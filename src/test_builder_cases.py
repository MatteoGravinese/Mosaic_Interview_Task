import unittest
import json
from builder_classes import visualization, layout, encoding
with open("valid_example_1.json") as f:
    EXAMPLE1 = json.load(f)
with open("valid_example_2.json") as f:
    EXAMPLE2 = json.load(f)
class TestBuilderClasses(unittest.TestCase):
    def test_generate_example1(self):
        json1 = layout().direction("vertical").gap("10px").add_child(
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
        if (json1 == EXAMPLE1):
            return("First Python build passes")
        else:
            return(self.assertEqual(json1, EXAMPLE1))

        
    def test_generate_example2(self):
        json2= layout().direction("horizontal").gap("14px").add_child(
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
        if (json2 == EXAMPLE2):
            print("Second Python build passes")
        else:
            self.assertEqual(json2, EXAMPLE2)
def test_generate_example1_output():
    suite = unittest.TestSuite()
    suite.addTest(TestBuilderClasses("test_generate_example1"))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
def test_generate_example2_output():
    suite = unittest.TestSuite()
    suite.addTest(TestBuilderClasses("test_generate_example2"))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)