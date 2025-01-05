package com.email.clasiffier.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.email.clasiffier.model.Email;
import com.email.clasiffier.service.SpamClasiffierService;

@RestController
@RequestMapping("/predict")
public class ClasiffierController {

    @Autowired
    private SpamClasiffierService spamClassifierService;

    @PostMapping
    public String classifyEmail(@RequestBody Email email) {
        try {
            return spamClassifierService.classify(email.getMailText());
        } catch (Exception e) {
            return "Error: " + e.getMessage();
        }
    }
}
