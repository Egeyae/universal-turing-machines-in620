//Syntax:

name: Unaire Multiplication
init: q0
accept: qAccept

// < = left
// > = right
// - = hold
// _ for blank cells

//-------DELTA FUNCTION:

#We read until the # and we write x in the second tape.
q0,1,_,_
q0,1,1,_,>,>,-


q0,#,_,_
q1,#,_,_,>,<,-

#If we have nothing when we go back, accept
q1,1,_,_
qAccept,1,_,_,-,-,-

# We decrease tape 2 who is the tape who say how many time we need to multiplicate y.
q1,1,1,_
q2,1,_,_,-,-,-

# We write in the third tape (result)
q2,1,_,_
q2,1,_,1,>,-,>

# We go back
q2,_,_,_
q3,_,_,_,<,-,-

# We go back until #
q3,1,_,_
q3,1,_,_,<,-,-

q3,#,_,_
q1,#,_,_,>,<,-

//States and symbols are case-sensitive
