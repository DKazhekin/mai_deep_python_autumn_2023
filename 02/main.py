import json
import time


def parse_json(json_str: str, keyword_callback=None, required_fields=None, keywords=None):
    try:
        json_doc = json.loads(json_str)
    except json.JSONDecodeError:
        print("Error! You need to set first argument as JSON string type!")
        exit(0)
    except TypeError:
        print("Error! Please, provide string type first argument")
        exit(0)

    if callable(keyword_callback) and required_fields is not None and keywords is not None:
        for key, value in json_doc.items():
            if key in required_fields:
                value = value.split(' ')
                for item in value:
                    if item in keywords:
                        keyword_callback(item)
    else:
        print(
            "Make sure that you provided 'keyword_callback',"
            " 'required_fields',"
            " 'keywords' arguments")


def mean(k):
    def timer(fn):
        def wrapper(value):

            start = time.time()
            res = fn(value)
            end = time.time()

            length = end - start
            wrapper.time.append(length)
            if len(wrapper.time) < k:
                print(sum(wrapper.time) / len(wrapper.time))
            else:
                print(sum(wrapper.time[len(wrapper.time) - k:len(wrapper.time)]) / len(wrapper.time))
            return res

        wrapper.time = []
        return wrapper

    return timer


@mean(5)
def print_upper(value: str):
    print(value.upper())


def main():
    json_string = '{"key1": "Word1 word2", "key2": "word2 word3"}'
    parse_json(json_string, print_upper, ["key2"], ["word3", "word2"])


if __name__ == '__main__':
    main()
