//-------CONFIGURATION
name: utm_states4_alpha2
init: start
accept: end

//-------INIT

// at start, simply skip and remove the first 1
start,1,_,_
gotoend,_,_,_,>,-,-

// then we should go the end of input
gotoend,0,_,_
gotoend,0,_,_,>,-,-

gotoend,1,_,_
gotoend,1,_,_,>,-,-

gotoend,#,_,_
gotoend,#,_,_,>,-,-

gotoend,_,_,_
copyXto3,_,_,_,<,-,-

// we copy the x to 3rd tape, right to left so it is easier
// we could do a bit of error detection by using 2 states (since alpha is 2 bits wide), but this is not done here
copyXto3,0,_,_
copyXto3,_,_,0,<,-,<

copyXto3,1,_,_
copyXto3,_,_,1,<,-,<

copyXto3,#,_,_
writeInitState1,_,0,_,-,>,-

writeInitState1,_,_,_
writeInitState2,_,0,_,-,>,-

writeInitState2,_,_,_
writeInitState3,_,0,_,-,>,-

writeInitState3,_,_,_
writeInitSymbol1,_,0,_,-,>,>

writeInitSymbol1,_,_,0
writeInitSymbol2,_,0,0,-,>,>

writeInitSymbol1,_,_,1
writeInitSymbol2,_,1,1,-,>,>

writeInitSymbol2,_,_,0
reset,_,0,0,-,-,-

writeInitSymbol2,_,_,1
reset,_,1,1,-,-,-

//-------RUN

// RESET tapes 1 and 2 to start the search
// starts with 0
reset,0,0,0
reset,0,0,0,<,<,-

reset,0,0,1
reset,0,0,1,<,<,-

reset,0,1,0
reset,0,1,0,<,<,-

reset,0,1,1
reset,0,1,1,<,<,-

reset,0,_,0
reset,0,_,0,<,-,-

reset,0,0,_
reset,0,0,_,<,<,-

reset,0,_,1
reset,0,_,1,<,-,-

reset,0,1,_
reset,0,1,_,<,<,-

// starts with 1
reset,1,0,0
reset,1,0,0,<,<,-

reset,1,0,1
reset,1,0,1,<,<,-

reset,1,1,0
reset,1,1,0,<,<,-

reset,1,1,1
reset,1,1,1,<,<,-

reset,1,_,0
reset,1,_,0,<,-,-

reset,1,0,_
reset,1,0,_,<,<,-

reset,1,_,1
reset,1,_,1,<,-,-

reset,1,1,_
reset,1,1,_,<,<,-

// starts with _
reset,_,0,0
reset,_,0,0,<,<,-

reset,_,0,1
reset,_,0,1,<,<,-

reset,_,1,0
reset,_,1,0,<,<,-

reset,_,1,1
reset,_,1,1,<,<,-

reset,_,0,_
reset,_,0,_,<,<,-

reset,_,1,_
reset,_,1,_,<,<,-

// end conditions
reset,_,_,0
ismatching,_,_,0,>,>,-

reset,_,_,1
ismatching,_,_,1,>,>,-

reset,_,_,_
ismatching,_,_,_,>,>,-

// ISMATCHING checks if current transition in code matches current state

// LOOP
ismatching,1,1,0
ismatching,1,1,0,>,>,-

ismatching,1,1,1
ismatching,1,1,1,>,>,-

ismatching,1,1,_
ismatching,1,1,_,>,>,-

ismatching,0,0,0
ismatching,0,0,0,>,>,-

ismatching,0,0,1
ismatching,0,0,1,>,>,-

ismatching,0,0,_
ismatching,0,0,_,>,>,-

// FOUND
ismatching,1,_,0
gotocurrstart,1,_,0,-,<,-

ismatching,1,_,1
gotocurrstart,1,_,1,-,<,-

ismatching,1,_,_
gotocurrstart,1,_,_,-,<,-

ismatching,0,_,0
gotocurrstart,0,_,0,-,<,-

ismatching,0,_,1
gotocurrstart,0,_,1,-,<,-

ismatching,0,_,_
gotocurrstart,0,_,_,-,<,-

// NOT MATCHING

ismatching,1,0,0
findnext,1,0,0,>,>,-

ismatching,1,0,1
findnext,1,0,1,>,>,-

ismatching,1,0,_
findnext,1,0,_,>,>,-

ismatching,0,1,0
findnext,0,1,0,>,>,-

ismatching,0,1,1
findnext,0,1,1,>,>,-

ismatching,0,1,_
findnext,0,1,_,>,>,-

// WRITENEXT
// GOTO CURR START
gotocurrstart,0,0,0
gotocurrstart,0,0,0,-,<,-

gotocurrstart,0,0,1
gotocurrstart,0,0,1,-,<,-

gotocurrstart,0,0,_
gotocurrstart,0,0,_,-,<,-

gotocurrstart,0,1,0
gotocurrstart,0,1,0,-,<,-

gotocurrstart,0,1,1
gotocurrstart,0,1,1,-,<,-

gotocurrstart,0,1,_
gotocurrstart,0,1,_,-,<,-

gotocurrstart,1,0,0
gotocurrstart,1,0,0,-,<,-

gotocurrstart,1,0,1
gotocurrstart,1,0,1,-,<,-

gotocurrstart,1,0,_
gotocurrstart,1,0,_,-,<,-

gotocurrstart,1,1,0
gotocurrstart,1,1,0,-,<,-

gotocurrstart,1,1,1
gotocurrstart,1,1,1,-,<,-

gotocurrstart,1,1,0
gotocurrstart,1,1,0,-,<,-


// end conditions of gotocurrstart
gotocurrstart,0,_,0
writecurrstate,0,_,0,-,>,-

gotocurrstart,0,_,1
writecurrstate,0,_,1,-,>,-

gotocurrstart,0,_,_
writecurrstate,0,_,_,-,>,-

gotocurrstart,1,_,0
writecurrstate,1,_,0,-,>,-

gotocurrstart,1,_,1
writecurrstate,1,_,1,-,>,-

gotocurrstart,1,_,_
writecurrstate,1,_,_,-,>,-

// WRITE TO CURR

writecurrstate,0,0,0
writecurrstate,0,0,0,>,>,-

writecurrstate,0,0,1
writecurrstate,0,0,1,>,>,-

writecurrstate,0,0,_
writecurrstate,0,0,_,>,>,-

writecurrstate,0,1,0
writecurrstate,0,0,0,>,>,-

writecurrstate,0,1,1
writecurrstate,0,0,1,>,>,-

writecurrstate,0,1,_
writecurrstate,0,0,_,>,>,-

writecurrstate,1,0,0
writecurrstate,1,1,0,>,>,-

writecurrstate,1,0,1
writecurrstate,1,1,1,>,>,-

writecurrstate,1,0,_
writecurrstate,1,1,_,>,>,-

writecurrstate,1,1,0
writecurrstate,1,1,0,>,>,-

writecurrstate,1,1,1
writecurrstate,1,1,1,>,>,-

writecurrstate,1,1,_
writecurrstate,1,1,_,>,>,-

writecurrstate,0,_,0
writesymbol1,0,_,0,-,<,-

writecurrstate,0,_,1
writesymbol1,0,_,1,-,<,-

writecurrstate,0,_,_
writesymbol1,0,_,_,-,<,-

writecurrstate,1,_,0
writesymbol1,1,_,0,-,<,-

writecurrstate,1,_,1
writesymbol1,1,_,1,-,<,-

writecurrstate,1,_,_
writesymbol1,1,_,_,-,<,-


// WRITE SYMBOL

writesymbol1,0,0,0
writesymbol2,0,0,0,-,<,<

writesymbol1,0,0,1
writesymbol2,0,0,0,-,<,<

writesymbol1,0,0,_
writesymbol2,0,0,0,-,<,<

writesymbol1,0,1,0
writesymbol2,0,1,1,-,<,<

writesymbol1,0,1,1
writesymbol2,0,1,1,-,<,<

writesymbol1,0,1,_
writesymbol2,0,1,1,-,<,<

writesymbol1,1,0,0
writesymbol2,1,0,0,-,<,<

writesymbol1,1,0,1
writesymbol2,1,0,0,-,<,<

writesymbol1,1,0,_
writesymbol2,1,0,0,-,<,<

writesymbol1,1,1,0
writesymbol2,1,1,1,-,<,<

writesymbol1,1,1,1
writesymbol2,1,1,1,-,<,<

writesymbol1,1,1,_
writesymbol2,1,1,1,-,<,<


writesymbol2,0,0,0
move1,0,0,0,-,>,>

writesymbol2,0,0,1
move1,0,0,0,-,>,>

writesymbol2,0,0,_
move1,0,0,0,-,>,>

writesymbol2,0,1,0
move1,0,1,1,-,>,>

writesymbol2,0,1,1
move1,0,1,1,-,>,>

writesymbol2,0,1,_
move1,0,1,1,-,>,>

writesymbol2,1,0,0
move1,1,0,0,-,>,>

writesymbol2,1,0,1
move1,1,0,0,-,>,>

writesymbol2,1,0,_
move1,1,0,0,-,>,>

writesymbol2,1,1,0
move1,1,1,1,-,>,>

writesymbol2,1,1,1
move1,1,1,1,-,>,>

writesymbol2,1,1,_
move1,1,1,1,-,>,>



// MOVEMENT
// 1 for RIGHT, 0 for LEFT => 00 = 1 move LEFT, 11 = 1 move RIGHT, 01 or 10 = STAY PUT

move1,1,0,0
move2,1,0,0,>,-,>

move1,1,0,1
move2,1,0,1,>,-,>

move1,1,0,_
move2,1,0,_,>,-,>

move1,1,1,0
move2,1,1,0,>,-,>

move1,1,1,1
move2,1,1,1,>,-,>

move1,1,1,_
move2,1,1,_,>,-,>

move1,0,0,0
move2,0,0,0,>,-,<

move1,0,0,1
move2,0,0,1,>,-,<

move1,0,0,_
move2,0,0,_,>,-,<

move1,0,1,0
move2,0,1,0,>,-,<

move1,0,1,1
move2,0,1,1,>,-,<

move1,0,1,_
move2,0,1,_,>,-,<

// MOVE2

move2,1,0,0
writereadinghead,1,0,0,>,-,>

move2,1,0,1
writereadinghead,1,0,1,>,-,>

move2,1,0,_
writereadinghead,1,0,_,>,-,>

move2,1,1,0
writereadinghead,1,1,0,>,-,>

move2,1,1,1
writereadinghead,1,1,1,>,-,>

move2,1,1,_
writereadinghead,1,1,_,>,-,>

move2,0,0,0
writereadinghead,0,0,0,>,-,<

move2,0,0,1
writereadinghead,0,0,1,>,-,<

move2,0,0,_
writereadinghead,0,0,_,>,-,<

move2,0,1,0
writereadinghead,0,1,0,>,-,<

move2,0,1,1
writereadinghead,0,1,1,>,-,<

move2,0,1,_
writereadinghead,0,1,_,>,-,<

// WRITE READING HEAD

writereadinghead,1,0,0
writereadinghead1,1,0,0,-,<,<

writereadinghead,1,1,0
writereadinghead1,1,0,0,-,<,<

writereadinghead,1,0,1
writereadinghead1,1,1,1,-,<,<

writereadinghead,1,1,1
writereadinghead1,1,1,1,-,<,<

writereadinghead,1,0,_
writereadinghead1,1,1,1,-,<,<

writereadinghead,1,1,_
writereadinghead1,1,1,1,-,<,<

writereadinghead,0,0,0
writereadinghead1,0,0,0,-,<,<

writereadinghead,0,1,0
writereadinghead1,0,0,0,-,<,<

writereadinghead,0,0,1
writereadinghead1,0,1,1,-,<,<

writereadinghead,0,1,1
writereadinghead1,0,1,1,-,<,<

writereadinghead,0,0,_
writereadinghead1,0,1,1,-,<,<

writereadinghead,0,1,_
writereadinghead1,0,1,1,-,<,<

writereadinghead,_,0,0
writereadinghead1,_,0,0,<,<,<

writereadinghead,_,1,0
writereadinghead1,_,0,0,<,<,<

writereadinghead,_,0,1
writereadinghead1,_,1,1,<,<,<

writereadinghead,_,1,1
writereadinghead1,_,1,1,<,<,<

writereadinghead,_,0,_
writereadinghead1,_,1,1,<,<,<

writereadinghead,_,1,_
writereadinghead1,_,1,1,<,<,<

writereadinghead,_,0,0
writereadinghead1,_,0,0,<,<,<

writereadinghead,_,1,0
writereadinghead1,_,0,0,<,<,<

writereadinghead,_,0,1
writereadinghead1,_,1,1,<,<,<

writereadinghead,_,1,1
writereadinghead1,_,1,1,<,<,<

writereadinghead,_,0,_
writereadinghead1,_,1,1,<,<,<

writereadinghead,_,1,_
writereadinghead1,_,1,1,<,<,<

writereadinghead1,1,1,1
checkend,1,1,1,-,<,>

writereadinghead1,1,1,0
checkend,1,0,0,-,<,>

writereadinghead1,1,1,_
checkend,1,1,1,-,<,>

writereadinghead1,1,0,1
checkend,1,1,1,-,<,>

writereadinghead1,1,0,0
checkend,1,0,0,-,<,>

writereadinghead1,1,0,_
checkend,1,1,1,-,<,>

writereadinghead1,0,1,1
checkend,0,1,1,-,<,>

writereadinghead1,0,1,0
checkend,0,0,0,-,<,>

writereadinghead1,0,1,_
checkend,0,1,1,-,<,>

writereadinghead1,0,0,1
checkend,0,1,1,-,<,>

writereadinghead1,0,0,0
checkend,0,0,0,-,<,>

writereadinghead1,0,0,_
checkend,0,1,1,-,<,>



// FIND NEXT
// Starts by going at the end of the curr state, then we know the size until next possible transition
// If next possible is _, then it means we can reject x with <M>


findnext,1,1,1
findnext,1,1,1,>,>,-

findnext,1,1,0
findnext,1,1,0,>,>,-

findnext,1,1,_
findnext,1,1,_,>,>,-

findnext,1,0,1
findnext,1,0,1,>,>,-

findnext,1,0,0
findnext,1,0,0,>,>,-

findnext,1,0,_
findnext,1,0,_,>,>,-

findnext,0,1,1
findnext,0,1,1,>,>,-

findnext,0,1,0
findnext,0,1,0,>,>,-

findnext,0,1,_
findnext,0,1,_,>,>,-

findnext,0,0,1
findnext,0,0,1,>,>,-

findnext,0,0,0
findnext,0,0,0,>,>,-

findnext,0,0,_
findnext,0,0,_,>,>,-

findnext,1,_,0
findnext1,1,_,0,>,-,-

findnext,0,_,0
findnext1,0,_,0,>,-,-

findnext1,1,_,0
findnext2,1,_,0,>,-,-

findnext1,0,_,0
findnext2,0,_,0,>,-,-

findnext2,1,_,0
findnext3,1,_,0,>,-,-

findnext2,0,_,0
findnext3,0,_,0,>,-,-

findnext3,1,_,0
findnext4,1,_,0,>,-,-

findnext3,0,_,0
findnext4,0,_,0,>,-,-

findnext4,1,_,0
findnext5,1,_,0,>,-,-

findnext4,0,_,0
findnext5,0,_,0,>,-,-

findnext5,1,_,0
findnext6,1,_,0,>,-,-

findnext5,0,_,0
findnext6,0,_,0,>,-,-

findnext6,1,_,0
findnext7,1,_,0,>,-,-

findnext6,0,_,0
findnext7,0,_,0,>,-,-

findnext,1,_,1
findnext1,1,_,1,>,-,-

findnext,0,_,1
findnext1,0,_,1,>,-,-

findnext1,1,_,1
findnext2,1,_,1,>,-,-

findnext1,0,_,1
findnext2,0,_,1,>,-,-

findnext2,1,_,1
findnext3,1,_,1,>,-,-

findnext2,0,_,1
findnext3,0,_,1,>,-,-

findnext3,1,_,1
findnext4,1,_,1,>,-,-

findnext3,0,_,1
findnext4,0,_,1,>,-,-

findnext4,1,_,1
findnext5,1,_,1,>,-,-

findnext4,0,_,1
findnext5,0,_,1,>,-,-

findnext5,1,_,1
findnext6,1,_,1,>,-,-

findnext5,0,_,1
findnext6,0,_,1,>,-,-

findnext6,1,_,1
findnext7,1,_,1,>,-,-

findnext6,0,_,1
findnext7,0,_,1,>,-,-

findnext,1,_,_
findnext1,1,_,_,>,-,-

findnext,0,_,_
findnext1,0,_,_,>,-,-

findnext1,1,_,_
findnext2,1,_,_,>,-,-

findnext1,0,_,_
findnext2,0,_,_,>,-,-

findnext2,1,_,_
findnext3,1,_,_,>,-,-

findnext2,0,_,_
findnext3,0,_,_,>,-,-

findnext3,1,_,_
findnext4,1,_,_,>,-,-

findnext3,0,_,_
findnext4,0,_,_,>,-,-

findnext4,1,_,_
findnext5,1,_,_,>,-,-

findnext4,0,_,_
findnext5,0,_,_,>,-,-

findnext5,1,_,_
findnext6,1,_,_,>,-,-

findnext5,0,_,_
findnext6,0,_,_,>,-,-

findnext6,1,_,_
findnext7,1,_,_,>,-,-

findnext6,0,_,_
findnext7,0,_,_,>,-,-


findnext7,0,_,0
resetcurr,0,_,0,>,<,-

resetcurr,0,0,0
resetcurr,0,0,0,-,<,-

resetcurr,0,1,0
resetcurr,0,1,0,-,<,-

resetcurr,0,_,0
ismatching,0,_,0,-,>,-

findnext7,0,_,1
resetcurr,0,_,1,>,<,-

resetcurr,0,0,1
resetcurr,0,0,1,-,<,-

resetcurr,0,1,1
resetcurr,0,1,1,-,<,-

resetcurr,0,_,1
ismatching,0,_,1,-,>,-

findnext7,0,_,_
resetcurr,0,_,_,>,<,-

resetcurr,0,0,_
resetcurr,0,0,_,-,<,-

resetcurr,0,1,_
resetcurr,0,1,_,-,<,-

resetcurr,0,_,_
ismatching,0,_,_,-,>,-

findnext7,1,_,0
resetcurr,1,_,0,>,<,-

resetcurr,1,0,0
resetcurr,1,0,0,-,<,-

resetcurr,1,1,0
resetcurr,1,1,0,-,<,-

resetcurr,1,_,0
ismatching,1,_,0,-,>,-

findnext7,1,_,1
resetcurr,1,_,1,>,<,-

resetcurr,1,0,1
resetcurr,1,0,1,-,<,-

resetcurr,1,1,1
resetcurr,1,1,1,-,<,-

resetcurr,1,_,1
ismatching,1,_,1,-,>,-

findnext7,1,_,_
resetcurr,1,_,_,>,<,-

resetcurr,1,0,_
resetcurr,1,0,_,-,<,-

resetcurr,1,1,_
resetcurr,1,1,_,-,<,-

resetcurr,1,_,_
ismatching,1,_,_,-,>,-




// CHECK END
// Here we check if curr state is 0001 <=> end state, we use 2 states for this

checkend,1,1,0
checkend0,1,1,0,-,<,-

checkend,1,1,1
checkend0,1,1,1,-,<,-

checkend,1,1,_
checkend0,1,1,_,-,<,-

checkend,0,1,0
checkend0,0,1,0,-,<,-

checkend,0,1,1
checkend0,0,1,1,-,<,-

checkend,0,1,_
checkend0,0,1,_,-,<,-


checkend0,1,0,1
checkend0,1,0,1,-,<,-

checkend0,1,0,0
checkend0,1,0,0,-,<,-

checkend0,1,0,_
checkend0,1,0,_,-,<,-

checkend0,0,0,1
checkend0,0,0,1,-,<,-

checkend0,0,0,0
checkend0,0,0,0,-,<,-

checkend0,0,0,_
checkend0,0,0,_,-,<,-

checkend0,0,1,0
reset,0,1,0,-,<,-

checkend0,0,_,0
end,0,_,0,-,-,-

checkend,0,0,0
reset,0,0,0,-,-,-

checkend0,0,1,1
reset,0,1,1,-,<,-

checkend0,0,_,1
end,0,_,1,-,-,-

checkend,0,0,1
reset,0,0,1,-,-,-

checkend0,0,1,_
reset,0,1,_,-,<,-

checkend0,0,_,_
end,0,_,_,-,-,-

checkend,0,0,_
reset,0,0,_,-,-,-

checkend0,1,1,0
reset,1,1,0,-,<,-

checkend0,1,_,0
end,1,_,0,-,-,-

checkend,1,0,0
reset,1,0,0,-,-,-

checkend0,1,1,1
reset,1,1,1,-,<,-

checkend0,1,_,1
end,1,_,1,-,-,-

checkend,1,0,1
reset,1,0,1,-,-,-

checkend0,1,1,_
reset,1,1,_,-,<,-

checkend0,1,_,_
end,1,_,_,-,-,-

checkend,1,0,_
reset,1,0,_,-,-,-