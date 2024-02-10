---
layout: activity
permalink: /Activities/DigitalSignatures
title: "Web and Mobile Development - Digital Signatures"


info:
  goals: 
    - To explain and execute the process for public-key cryptography
    - To explain how public key cryptography is used to generate a digital signature that enforces non-repudiation
  models:
    - model: |    
        <img src="../images/activity-digitalsignatures/csunplugged-public-map.png" alt="Public Key Map from CSUnplugged, shared under a Creative Commons BY-NC-SA 4.0 License">
      title: Public-Key Cryptography
      questions:
        - Choose a secret numeric value that you want to send securely to a partner.
        - Fill in the nodes of the public map with integers that add up to the secret value you chose.
        - For each node, replace the value with the sum of itself plus the original value found in the adjacent neighbors.
        - Send this graph to your partner.  Can your partner figure out the value without any help (probably not!)?
        - Your partner (and only your partner) should look at the Private Map (see below), which highlights the nodes that should be added together to obtain the value.
        - How did this work?  If every student used a unique "map," how could you use this approach to send data securely to anyone?
    - model: |    
        <img src="../images/activity-digitalsignatures/csunplugged-public-map2.png" alt="Public Key Map from CSUnplugged, shared under a Creative Commons BY-NC-SA 4.0 License">
      title: Digital Signatures
      questions:
        - If I encrypt something using someone's private map, who can decode it?
        - If I encrypt something using my own public map, who can decode it?
        - How could you use these maps to ensure that a particular person actually sent a particular value?
        - How can I use this approach to ensure that the data that I sent was not altered along the way?
        
tags:
  - cryptography
  - signatures
  
---

The CS Unplugged Materials are shared by [CSUnplugged](https://classic.csunplugged.org/public-key-encryption/) under a [Creative Commons BY-NC-SA 4.0 License](http://creativecommons.org/licenses/by-nc-sa/4.0/).

The Private Map for this activity can be found [here](../images/activity-digitalsignatures/csunplugged-private-map.png) and [here](../images/activity-digitalsignatures/csunplugged-private-map2.png)