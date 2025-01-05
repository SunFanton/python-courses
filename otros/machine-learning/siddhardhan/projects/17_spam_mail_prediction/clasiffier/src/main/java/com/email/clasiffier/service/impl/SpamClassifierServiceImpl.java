package com.email.clasiffier.service.impl;

import java.io.FileInputStream;
import java.util.List;
import java.util.Map;

import org.dmg.pmml.PMML;
import org.jpmml.evaluator.Evaluator;
import org.jpmml.evaluator.InputField;
import org.jpmml.evaluator.ModelEvaluatorBuilder;
import org.jpmml.evaluator.ProbabilityDistribution;
import org.jpmml.evaluator.TargetField;
import org.jpmml.model.PMMLUtil;
import org.springframework.stereotype.Service;

import com.email.clasiffier.service.SpamClasiffierService;

import jakarta.annotation.PostConstruct;

@Service
public class SpamClassifierServiceImpl implements SpamClasiffierService {

	private Evaluator evaluator;
	private String inputField, targetField;
	
	@PostConstruct
	public void loadModel() throws Exception {
        // Cargar el archivo PMML desde la carpeta resources
        FileInputStream fis = new FileInputStream(getClass().getClassLoader().getResource("email_classifier.pmml").getFile());
        PMML pmml = PMMLUtil.unmarshal(fis);

        // Compilar el modelo PMML
        ModelEvaluatorBuilder modelEvaluatorBuilder = new ModelEvaluatorBuilder(pmml);

        evaluator = modelEvaluatorBuilder.build();
        
        
        // Printing input (x1, x2, .., xn) fields
        List<InputField> inputFields = evaluator.getInputFields();
        System.out.println("Input fields: " + inputFields);
        inputField = inputFields.get(0).getFieldName();

        // Printing primary result (y) field(s)
        List<TargetField> targetFields = evaluator.getTargetFields();
        System.out.println("Target field(s): " + targetFields);
        targetField = targetFields.get(0).getFieldName();
        
        /*
        // Printing secondary result (eg. probability(y), decision(y)) fields
        List<OutputField> outputFields = evaluator.getOutputFields();
        System.out.println("Output fields: " + outputFields);*/
    }

	
	@SuppressWarnings("unchecked")
	@Override
	public String classify(String text) throws Exception {
		
		// Crear un mapa con los datos de entrada (en este caso, el texto del email)
        Map<String, ?> arguments = Map.of(
            inputField, text
        );

        // Realizar la predicción
        Map<String, ?> results = evaluator.evaluate(arguments);
        ProbabilityDistribution<Number> prob = (ProbabilityDistribution<Number>) results.get(targetField);

        Object prediction = prob.getResult();
        String result = prediction != null ? prediction.toString() : "Unknown";
        
        if(!result.equalsIgnoreCase("Unknown")) {
        	result = result.equals("0") ? "Spam" : "Not spam";
        }
        
        return result;
	}

}
