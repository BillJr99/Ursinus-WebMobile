---
layout: activity
permalink: /Activities/VirtualMemory2
title: "Virtual Memory"
excerpt: "Virtual Memory"

info:
  prev: ./VirtualMemory
  next: ./VirtualMemory3
  
  goals: 
    - To explain why memory is segmented into a stack and heap
    - To reason about the benefits of growing the stack and heap in opposite directions
    - To motivate the need for virtual memory, and specifically, for logical addressing
    - To design a logical address space that facilitates cooperative multitasking
  models:
    - model: |
        <script type="syntaxhighlighter" class="brush: mips"><![CDATA[
        .data 
        str1: .asciiz "Five plus two is: "

        .text
        main:
            # Make room on the stack
            sub $sp, $sp, 4 
            
            # Load the values 5 and 2 and add them together
            li $t0, 5
            li $t1, 2
            add $t2, $t0, $t1

            # Store the result on the stack
            sw $t2, 0($sp)

            # Print the string at the address specified by str1
            li $v0, 4
            la $a0, str1
            syscall
         
            # Print the sum from the stack
            li $v0, 1
            lw $a0, 0($sp)
            syscall

            # Pop the stack back to the way we found it
            add $sp, $sp, 4
            
            # ... and quit!
            li $v0, 10
            syscall        
        ]]></script>
        <br>
        <img src="../images/activity-virtualmemory/sum-mem.png" alt="A MIPS program running with its memory laid out across its various segments.">
        <br>
        <img src="../images/activity-virtualmemory/sum-prog.png" alt="A snippet of MIPS code for the program that generated this memory layout.">
      title: "Mapping the MIPS Address Space"
      questions:
        - "What address contains the value 7 from the program above?"
        - "In what region of memory is this value 7 located?"
        - "What address contains the string &quot;Five plus two is&quot;, and in what region is this located?"
        - "What addresses contain code, and in what region are these lines of code stored?"
        - "What would happen to our memory layout if you wanted to load and run another program?"
        - "Why is it important to have a consistent memory layout for each program we compile?  In other words, why not just randomize where things go in our program so that it is less likely that programs interfere with one another?"        
    
tags:
  - virtualmemory
  
---

