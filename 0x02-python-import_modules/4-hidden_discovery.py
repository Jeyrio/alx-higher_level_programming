#!/usr/bin/python3

import importlib

if __name__ == "__main__":
    module = imp.load_compiled("hidden_4.pyc", ".")

names = []
for name in module.dict:
        if name != "__":
            names.append(name)
            names.sort()
            for name in names:
                print(name)
