import xml.etree.ElementTree as ET
import sys

elements =  {
    'svg':            ('version', 'baseProfile', 'width', 'viewBox', 'preserveAspectRatio', 'snapshotTime'),
    'g':              (),
    'defs':           (),
    'title':          (),
    'desc':           (),
    'use':            ('x', 'y', 'xlink:href'),
    'rect':           ('x', 'y', 'width', 'height', 'rx', 'ry'),
    'circle':         ('cx', 'cy', 'r'),
    'ellipse':        ('cx', 'cy', 'rx', 'ry'),
    'line':           ('x1', 'y1', 'x2', 'y2'),
    'polyline':       ('points'),
    'polygon':        ('points'),
    'text':           ('x', 'y', 'rotate'),
    'tspan':          (),
    'textArea':       ('x', 'y', 'width', 'height', 'auto'),
    'tbreak':         (),
    'solidcolor':     (),
    'linearGradient': ('gradientUnits', 'x1', 'y1', 'x2', 'y2'),
    'radialGradient': ('gradientUnits', 'cx', 'cy', 'r'),
    'stop':           ('offset')
}

def check(el):
    if el.tag not in elements:
        print 'ERROR element "%s" not allowed' % (el.tag)
    else:
        ats = elements[el.tag]
        for name, val in el.attrib.items():
            if name not in ats:
                print 'ERROR element "%s" does not allow attribute "%s"' % (el.tag, name)
    for child in el:
        check(child)

def checkFile(fn):
    tree = ET.parse(fn)
    check(tree.getroot())

if __name__ == "__main__":
    for arg in sys.argv[1:]:
        checkFile(arg)
