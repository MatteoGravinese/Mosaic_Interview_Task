from builder_classes import visualization, layout, encoding
EXAMPLE1 = {
    "type": "layout",
    "direction": "vertical",
    "gap": "10px",
    "children": [
        {
            "type": "visualization",
            "mark": "bar",
            "encoding": {
                "x": "Temperature",
                "y": "Frequency",
                "color": "blue"
            }
        },
        {
            "type": "layout",
            "direction": "horizontal",
            "gap": "30px",
            "children": [
                {
                    "type": "visualization",
                    "mark": "line",
                    "encoding": {
                        "x": "Altitude",
                        "y": "Air Pressure",
                        "color": "orange"
                    }
                }
            ]
        },
        {
            "type": "visualization",
            "mark": "line",
            "encoding": {
                "x": "Time",
                "y": "Distance",
                "color": "cyan"
            }
        }
    ]
}
EXAMPLE2 = {
    "type": "layout",
    "direction": "horizontal",
    "gap": "14px",
    "children": [
        {
            "type": "visualization",
            "mark": "point",
            "encoding": {
                "x": "IQ",
                "y": "Weight",
                "color": "red"
            }
        },
        {
            "type": "layout",
            "direction": "vertical",
            "gap": "33px",
            "children": [
                {
                    "type": "visualization",
                    "mark": "area",
                    "encoding": {
                        "x": "Car Brand",
                        "y": "Percentage of Cars",
                        "color": "green"
                    }
                }
            ]
        }
    ]
}

def generate_example1():
    return layout().direction("vertical").gap("10px").add_child(
        visualization()
            .mark("bar")
            .add_encoding(
                encoding()
                    .channel("x").field("Temperature")
                    .channel("y").field("Frequency")
                    .channel("color").field("blue")
            ),
        layout().direction("horizontal").gap("30px").add_child(
            visualization()
                .mark("line")
                .add_encoding(
                    encoding()
                        .channel("x").field("Altitude")
                        .channel("y").field("Air Pressure")
                        .channel("color").field("orange")
                )
        ),
        visualization()
            .mark("line")
            .add_encoding(
                encoding()
                    .channel("x").field("Time")
                    .channel("y").field("Distance")
                    .channel("color").field("cyan")
            )
    ).build()
def generate_example2():
    return layout().direction("horizontal").gap("14px").add_child(
        visualization()
            .mark("point")
            .add_encoding(
                encoding()
                    .channel("x").field("IQ")
                    .channel("y").field("Weight")
                    .channel("color").field("red")
            ),
        layout().direction("vertical").gap("33px").add_child(
            visualization()
                .mark("area")
                .add_encoding(
                    encoding()
                        .channel("x").field("Car Brand")
                        .channel("y").field("Percentage of Cars")
                        .channel("color").field("green")
                )
        )
    ).build()
def test_builder1():
    if generate_example1() == EXAMPLE1:
        return "Python Code 1 Passes."
    else:
        return "Python Code 1 Fails."
def test_builder2():
    if generate_example2() == EXAMPLE2:
        return "Python Code 2 Passes."
    else:
        return "Python Code 2 Fails."