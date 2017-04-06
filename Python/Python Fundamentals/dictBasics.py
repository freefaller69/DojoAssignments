me = {
    "name":"Michael",
    "age":"48",
    "cob":"USA",
    "language":"elvish"
}

def aboutMe(dict):
    for key, data in dict.iteritems():
        print key, "=", data
    print "My name is", me["name"]
    print "My age is", me["age"]
    print "My country of birth is the good ol", me["cob"]
    print "My favorite language is", me["language"]
aboutMe(me)
