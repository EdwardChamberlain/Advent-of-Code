import cube_tools


initial_state = [[
    '.#.',
    '..#',
    '###',
]]



print("Initial")
cube_tools.render_cube(initial_state)

cube = cube_tools.expand_cube(initial_state)

for i in range(5):
    cube = cube_tools.expand_cube(cube)
print("After Expansion")
cube_tools.render_cube(cube)

print("Flipping")
for _ in range(3):
    cube = cube_tools.cycle_cube(cube)
    cube_tools.render_cube(cube)

print(cube_tools.sum_active_states(cube))
