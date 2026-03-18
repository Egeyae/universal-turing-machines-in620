//Syntax:

name: Linear Search
init: init
accept: valid

// < = left
// > = right
// - = hold
// _ for blank cells

//States and symbols are case-sensitive

// Copy x to tape 2
init,0,_
init,_,0,>,>

init,1,_
init,_,1,>,>

init,#,_
bad,#,_,-,<

// Go back to start of x if we are in bad state 
bad,#,0
bad,#,0,-,<

bad,#,1
bad,#,1,-,<

bad,#,_
read,#,_,>,>

// Reads until mismatch or end, if mismatch goes to end
// good match
read,0,0
read,0,0,>,>

read,1,1
read,1,1,>,>

// mismatch
read,0,1
end,0,1,>,>

read,1,0
end,1,0,>,>

// end of wi
read,#,0
bad,#,0,-,<

read,#,1
bad,#,1,-,<

// end of x
read,0,_
end,0,_,>,-

read,1,_
end,1,_,>,-

// end of x + wi => valid
read,#,_
valid,#,_,-,-

read,_,_
valid,_,_,-,-

// go to end of word
end,0,1
end,0,1,>,-

end,1,0
end,1,0,>,-

end,0,0
end,0,0,>,-

end,1,1
end,1,1,>,-

end,0,_
end,0,_,>,-

end,1,_
end,1,_,>,-

end,#,0
bad,#,0,-,<

end,#,1
bad,#,1,-,<

end,#,_
bad,#,_,-,<

// go to end of x
bad,#,1
bad,#,1,-,<

bad,#,0
bad,#,0,-,<

bad,#,_
read,#,_,>,>