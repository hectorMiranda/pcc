module twisted_text(text_str, twist_angle, height, size) {
    for (z = [0:0.5:height]) {
        translate([0, 0, z])
        rotate([0, 0, twist_angle * z / height])
        linear_extrude(height = 0.6)
            text(text_str, size = size, font = "Arial");
    }
}

twisted_text("marcetux", 360, 120, 10);
