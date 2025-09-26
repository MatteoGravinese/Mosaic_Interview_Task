import json
def function():
    class Encoding:
        def __init__(self):
            self._channels = {}
        def channel(self, name):
            self._current_channel = name
            return self
        def field(self, fieldsname):
            self._channels[self._current_channel] = fieldsname
            self._current_channel = None
            return self
        def build(self):
            return self._channels
    class Visualization:
        def __init__(self):
            self._mark = None
            self._encoding = None
        def mark(self, marktype):
            self._mark = marktype
            return self
        def add_encoding(self, encoding):
            self._encoding = encoding.build()
            return self
        def build(self):
            return {
                "type": "Visualization",
                "mark": self._mark,
                "encoding": self._encoding
            }
    class Layout:
        def __init__(self):
            self._direction = None
            self._gap = None
            self._children = []
        def direction(self, dirn):
            self._direction = dirn
            return self
        def gap(self, gap):
            self._gap = gap
            return self
        def add_child(self, *children):
            for child in children:
                self._children.append(child.build())
            return self
        def build(self):
            return{
                "type": "Layout",
                "direction": self._direction,
                "gap": self._gap,
                "children": self._children
            }
    def encoding(): return Encoding() 
    def visualization(): return Visualization() 
    def layout(): return Layout()
    spec = layout().direction("vertical").gap("10px").add_child(
        layout().direction("horizontal").gap("23px").add_child(
            visualization()
                .mark("line")
                .add_encoding(
                    encoding()
                        .channel("x").field("Time")
                        .channel("y").field("Distance")
                )
        ),
        visualization()
            .mark("bar")
            .add_encoding(
                encoding()
                    .channel("x").field("Weather")
                    .channel("y").field("People")
            )
    )
    return json.dumps(spec.build(), indent=2)
function()