from http_response_code import responses

l = []
for k, v in responses.items():
    l.append([str(k), v[0], v[1].replace(", ", " ")])

with open("output_en.csv", "+a") as foo:
    foo.write("code, title, description\n")
    for i in l:
        foo.write(", ".join(i))
        foo.write("\n")
