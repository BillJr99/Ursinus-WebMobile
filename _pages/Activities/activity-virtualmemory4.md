---
layout: activity
permalink: /Activities/VirtualMemory4
title: "Virtual Memory"
excerpt: "Virtual Memory"

info:
  prev: ./VirtualMemory3
  next: ./VirtualMemory5

  goals: 
    - To explain why memory is segmented into a stack and heap
    - To reason about the benefits of growing the stack and heap in opposite directions
    - To motivate the need for virtual memory, and specifically, for logical addressing
    - To design a logical address space that facilitates cooperative multitasking
  models:
    - model: |
        <a href="../images/activity-virtualmemory/CompileExample1.mp4"><img src="../images/activity-virtualmemory/CompileExample1-still.png" alt="An example C program that allocates two integers, adds them together, and stores their sum in an uninitialized global variable"></a>
      title: "Mapping a C Program to Memory"
      questions:
        - "To what sections does each highlighted portion of code compile in a C program?"
        - "What is the address of the two malloc'ed values?  How about the integer variables <code>a</code> and <code>b</code>?"
        - "When you access a and b, what accesses take place to get to the heap?"
    
tags:
  - virtualmemory
  
---

