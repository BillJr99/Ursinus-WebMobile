---
layout: activity
permalink: /Activities/SSL
title: "Web and Mobile Development - Secure Sockets Layer"


info:
  goals: 
    - To explain the process underlying SSL and the digital certificate for authentication and encryption
    - To create and attach a digital certificate to a RESTful service in node.js
  models:
    - model: |
        <div align="left">
        <pre>
        <code>
        const express = require('express')
        const https = require('https')
        
        const app = express();
        
        // Usual routes
        app.get('/test', (req, res) => {
            res.send("Hello World!");
        });
        
        const sslOptions = {
            key: fs.readFileSync('./private_key.pem'),
            cert: fs.readFileSync('./certificate_chain.pem'),
            ca: [
                fs.readFileSync('./cert_authority.cer') //,      
                // ...
            ],
            ciphers: [
                "ECDHE-RSA-AES128-SHA256",
                "DHE-RSA-AES128-SHA256",
                "AES128-GCM-SHA256",
                "RC4",
                "HIGH",
                "!MD5",
                "!aNULL"
                ].join(':'),            
        };
        
        const httpsServer = https.createServer(sslOptions, app);
        httpsServer.listen(8443, () => {
            console.log("HTTPS Running");
        });
        
        // I suggest omitting this, otherwise you have a route that can be invoked in clear text!
        const httpServer = http.createServer(app);
        httpServer.listen(8080, () => {
            console.log("HTTP Running");
        });
        </code>
        </pre>
        </div>
      title: SSL Certificates
      embed: <iframe height="400px" width="100%" src="https://repl.it/@BillJr99/RESTfulServiceExample?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>       
      questions:
        - What is an SSL Certificate Chain?
        - What is a Certificate Authority?
        - "Using this command, generate and use your own SSL certificate: <code>openssl genrsa -out private_key.pem && openssl req -new -key private_key.pem -out csr.pem && openssl x509 -req -days 9999 -in csr.pem -signkey private_key.pem -out certificate_chain.pem</code>.  Add these to a node.js program and invoke an endpoint over https."
        - Did you get a warning from your browser and, if so, why?
    - model: |
        <a title="I, Giaros / CC BY-SA (http://creativecommons.org/licenses/by-sa/3.0/)" href="https://commons.wikimedia.org/wiki/File:PublicKeyCertificateDiagram_It.svg"><img width="512" alt="PublicKeyCertificateDiagram It" src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/PublicKeyCertificateDiagram_It.svg/512px-PublicKeyCertificateDiagram_It.svg.png"></a>
      title: Signing of a Public Key by a Certificate Authority
      questions:
        - Although you can self-sign a certificate, why might it be more authoritative to have a trusted third party validate your identity and sign your key to form a certificate?
    - model: |
        <a href="https://tldp.org/HOWTO/SSL-Certificates-HOWTO/x64.html">Read this Article on SSL Certificates</a>
      questions:
        - Is the public/private key from the SSL certificate actually used to encrypt data between the client and server?  Why or why not?  If not, what is used instead?
      title: SSL Handshake and Encryption
tags:
  - ssl
  
---

