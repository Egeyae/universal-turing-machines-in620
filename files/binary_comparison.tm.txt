name: Binary Comparison
init: q0
accept: qF

// Ruban 1 : x#y
// Ruban 2 : copie de y

//We read x#y and copy y on the second ruban
q0,0,_
q0,0,_,>,>

q0,1,_
q0,1,_,>,>

q0,#,_
q1,_,_,>,>

q1,0,_
q1,_,0,>,>

q1,1,_
q1,_,1,>,>

//Once we finished copying y we go back to compare x with y 
q1,_,_
q2,_,_,<,<

q2,_,0
q2,_,0,<,-

q2,_,1
q2,_,1,<,-

//We compare x and y
q2,1,0
q3,1,0,-,-

q2,1,1
q3,1,1,-,-

q2,0,0
q3,0,0,-,- 

q2,0,1
q3,0,1,-,-

// if x = y then we continue
q3,0,0
q3,0,0,<,<

q3,1,1
q3,1,1,<,<

// x[i]=0, y[i]=1 : x < y we memorize in qL
q3,0,1
qL,0,1,<,<

// x[i]=1, y[i]=0 : x > y we memorize in qG
q3,1,0
qG,1,0,<,<

// x smaller than y : x < y : ACCEPT
q3,_,0
qF,_,0,-,-

q3,_,1
qF,_,1,-,-

q3,_,_
qLoop,_,_,>,>

qL,0,0
qL,0,0,>,>

qL,1,1
qL,1,1,>,>

qL,0,1
qL,0,1,>,>

qL,1,0
qG,1,0,>,>

qL,_,_
qF,_,_,-,-

qL,_,0
qF,_,0,-,-

qL,_,1
qF,_,1,-,-

qG,0,0
qG,0,0,>,>

qG,1,1
qG,1,1,>,>

qG,0,1
qL,0,1,>,>

qG,1,0
qG,1,0,>,>

// end : x > y we loop
qG,_,_
qLoop,_,_,-,-

qG,_,0
qLoop,_,0,-,-

qG,_,1
qLoop,_,1,-,-

qLoop,1,1
qLoop,1,1,>,>

qLoop,0,0
qLoop,0,0,>,>

qLoop,_,_
qLoop,_,_,-,-