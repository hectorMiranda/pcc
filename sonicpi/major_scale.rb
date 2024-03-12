# C Major Scale
use_bpm 100 # Set tempo

# Define the C Major scale notes
c_major_scale = [:C4, :D4, :E4, :F4, :G4, :A4, :B4, :C5]

# Play the scale ascending
c_major_scale.each do |note|
  play note
  sleep 0.5 # Wait for half a beat before playing the next note
end

# Play the scale descending
c_major_scale.reverse.each do |note|
  play note
  sleep 0.5 # Wait for half a beat before playing the next note
end