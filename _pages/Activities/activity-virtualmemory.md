---
layout: activity
permalink: /Activities/VirtualMemory
title: "Virtual Memory"
excerpt: "Virtual Memory"

info:
  goals: 
    - To explain why memory is segmented into a stack and heap
    - To reason about the benefits of growing the stack and heap in opposite directions
    - To motivate the need for virtual memory, and specifically, for logical addressing
    - To design a logical address space that facilitates cooperative multitasking
  models:
    - model: |
        <img src="../images/activity-virtualmemory/mips-address-space.png" alt="The MIPS address space includes a stack that begins at the top of the address space and grows downward, while the heap is in the lower region of the address space and grows upward.">
      title: "Warmup - MIPS Addresses"
      questions:
        - "Which region contains the translated machine code for your program?"
        - "Which address above is the starting address for a MIPS program?"
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
    - model: |
        <img src="https://www.vinylrecordlife.com/wp-content/uploads/2020/07/VINYL-RECORD-LIFE-TRACK-LISTING-1024x683.jpg?ezimgfmt=ng:webp/ngcb2" alt="Record showing tracks from vinylrecordlife.com"> 
      title: "Virtual Memory - Separating Programs with a Logical Address Space"
      questions:
        - "How might you describe to someone where to put the needle on the record to play the beginning of Track (program!) 1?"
        - "How about the beginning of Track 2?"
        - "What do you need to keep track of to know where the beginning of each song is located?"
        - "Where would you position the needle on the record to play Track 3 starting from the 1 minute mark?"
        - "How might we apply this idea to the memory layout of our programs so that we can compile them with a consistent layout, but also load multiple programs at the same time?"
    - model: |
        <a href="../images/activity-virtualmemory/CompileExample1.mp4"><img src="../images/activity-virtualmemory/CompileExample1-still.png" alt="An example C program that allocates two integers, adds them together, and stores their sum in an uninitialized global variable"></a>
      title: "Mapping a C Program to Memory"
      questions:
        - "To what sections does each highlighted portion of code compile in a C program?"
        - "What is the address of the two malloc'ed values?  How about the integer variables <code>a</code> and <code>b</code>?"
        - "When you access a and b, what accesses take place to get to the heap?"
    - model: |
        <a href="https://tinyurl.com/arraylistvector" target="_blank">Open the code visualizer below in a new window!</a>
        <br>
        <iframe src="https://tinyurl.com/arraylistvector" width="800" height="600">
      title: "Stack and Heap Access"
      questions:
        - "Trace through a few iterations of the program.  What happens to the local variables of each function as it is called?"
        - "What happens to those local variables when each function returns?"
        - "Why is it that we are able to access the vector across each function call, when the local variable storing its location is created as a local stack variable in <code>main</code>?"
        - "In the MIPS architecture, in what addresses might the local variables of each function be stored as they are called?"   
        
  reflective_prompts: 
    - "What would happen if you forgot to <code>free</code> your <code>malloc</code>'ed memory, and then your program terminated normally?"
    - "Why is it so important to call <code>free</code>?"
    - "What does the Operating System have to keep track of internally for each running program (&quot;process&quot;) in order to locate its stack variables?  In other words, given a logical address (which is not unique across programs), how do you determine the actual physical address in memory of that value?"
    
tags:
  - virtualmemory
  
---

