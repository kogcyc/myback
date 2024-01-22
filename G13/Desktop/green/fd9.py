from itertools import permutations
import sys
#
def generate_combinations(letters):
    if len(letters) != 3:
        raise ValueError("Input must be a three-letter string")
#
    letter_permutations = permutations(letters)
    combinations = [''.join(perm) for perm in letter_permutations]
#
    return combinations
#
# Example usage:
input_letters = sys.argv[1]
combinations = generate_combinations(input_letters)

tt = """.test {
  border: none;
  border-radius: 6px;
  padding: 0px 6px;
  outline: none;
  height: 25px;
  font-size: 16px;
  font-weight: 900;
  font-size: 13px;
  font-family: 'IBM Plex Mono', monospace;
  width: 90px;
  letter-spacing: 1px;
}

.w {color: #fff;}
"""

print("<head><style>")
print(f'{tt}')
for t in combinations:
    print(f'.c_{t} {{ background-color: #{t}; }}')
print("</style></head><body>")
for t in combinations:
    print(f'<input class="c_{t} test" value="#{t}" />')
print("</body>")