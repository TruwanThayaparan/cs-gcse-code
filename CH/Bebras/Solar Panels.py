width = float(input())
height = float(input())

panel_width = 0.95
panel_height = 1.5

panels_wide = int(width // panel_width)
panels_high = int(height // panel_height)

total_panels = panels_wide * panels_high

print(total_panels)
