# DFA
GUI for drawing Deterministic Finite Automatons (DFA) built using Python libraries tkinter and graphviz.

## Usage
./python DFA.py 

## Examples

### Example 1
Number of states: 3

Accept states: 0

Alphabet: a,b

Transitions: {"0":{"a":"1","b":"2"},"1":{"a":"0","b":"2"},"2":{"a":"2","b":"1"}}

![alt text](https://github.com/jackbullen/DFA/blob/main/pics/3state.jpg)

### Example 2
Number of states: 5

Accept states: 2,3,4

Alphabet: a,b

Transitions: {"0":{"a":"1","b":"2"},"1":{"a":"3","b":"4"},"2":{"a":"2","b":"3"},"3":{"a":"4","b":"3"},"4":{"a":"4","b":"4"}}

![alt text](https://github.com/jackbullen/DFA/blob/main/pics/5state.png)

### Example 3
Number of states: 14

Accept states: 0, 8, 9, 12

Alphabet: a,b,c,d,DEL,RES,ADD,SUB

Transitions: {"0":{"a":"1","b":"2","c":"3","d":"4","DEL":"5","RES":"6","ADD":"7","SUB":"8"},
"1":{"a":"9","b":"10","c":"11","d":"12","DEL":"13","RES":"7","ADD":"1","SUB":"4"},
"2":{"a":"7","b":"8","c":"9","d":"0","DEL":"2","RES":"2","ADD":"3","SUB":"4"},
"3":{"a":"4","b":"3","c":"13","d":"0","DEL":"2","RES":"9","ADD":"8","SUB":"7"},
"4":{"a":"6","b":"5","c":"14","d":"13","DEL":"12","RES":"11","ADD":"10","SUB":"9"},
"5":{"a":"7","b":"6","c":"5","d":"4","DEL":"3","RES":"2","ADD":"1","SUB":"0"},
"6":{"a":"8","b":"7","c":"6","d":"5","DEL":"4","RES":"3","ADD":"2","SUB":"1"},
"7":{"a":"6","b":"5","c":"4","d":"13","DEL":"12","RES":"11","ADD":"10","SUB":"9"},
"8":{"a":"4","b":"3","c":"12","d":"1","DEL":"3","RES":"9","ADD":"8","SUB":"7"},
"9":{"a":"1","b":"0","c":"3","d":"2","DEL":"5","RES":"4","ADD":"7","SUB":"6"},
"10":{"a":"0","b":"1","c":"2","d":"3","DEL":"4","RES":"5","ADD":"6","SUB":"7"},
"11":{"a":"3","b":"2","c":"1","d":"0","DEL":"7","RES":"6","ADD":"5","SUB":"4"},
"12":{"a":"2","b":"3","c":"0","d":"1","DEL":"6","RES":"7","ADD":"4","SUB":"5"},
"13":{"a":"7","b":"6","c":"5","d":"4","DEL":"3","RES":"2","ADD":"1","SUB":"0"}}

![alt text](https://github.com/jackbullen/DFA/blob/main/pics/25state.jpg)
