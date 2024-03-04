from music21 import stream, environment

# Set the path to the MuseScore executable
environment.set("musescoreDirectPNGPath", "/Applications/MuseScore 4.app/Contents/MacOS/mscore")

# Create a simple music stream with one measure
s = stream.Stream()
s.append(stream.Measure())

# Write the stream to a PNG file using MuseScore
s.write('musicxml.png', fp='test.png')