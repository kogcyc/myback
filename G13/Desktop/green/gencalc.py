a = []
a.append(["button_y_to_x","yx","process_y_to_x"])

for t in a:
	button = t[0]
	glyph = t[1]
	proc = t[2]

sp = f'<span id="{button}" class="button_class button_a">{glyph}</span>'

cnst = f'const {button} = document.getElementById("{button}");'

fnc = f'''
function {proc}() {{
  //stack_X.innerHTML = ;

  x_ready_for_new_input = true;
}}
'''

lst = f'''
{button}.addEventListener('click', function() {{
  {proc}();
}});
'''


print(sp + '\n')
print(cnst + '\n')
print(fnc + '\n')
print(lst + '\n')