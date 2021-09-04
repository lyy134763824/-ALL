import time
import json
# var
# e = p("#language").val().split("2")
# , t = p("#docUploadFile").val()
# , n = t.split(".")
# , r = n[n.length - 1]
# , i = t.split("\\")
# , o = i[i.length - 1]
# , a = p("#docUploadFile")[0].files
# , s = 1e3
# , l = (new Date).getTime()
# , c = p.md5("new-fanyiweb" + l + "ydsecret://newfanyiweb.doctran/sign/0j9n2{3mLSN-$Lg]K4o0N2}" + o);
# return a & & a[0] & & a[0].size & & (s = a[0].size),
# {
# from: e[0],
#       to: e[1],
# type: r,
# filename: o,
# client: "docserver",
# keyfrom: "new-fanyiweb",
# size: s,
# sign: c,
# salt: l
# }
#1630764336778
#1630763405414
data = {
'i':'time',
'from':'AUTO',
'to':'AUTO',
'smartresult':'dict',
'client':'fanyideskweb',
'salt':'16307632378073',
'sign':'77d640d6f90f4bb12544c299ab27c35f',
'lts':'1630763237807',
'bv':'89e18957825871c419be045180c67d3b',
'doctype':'json',
'version':'2.1',
'keyfrom':'fanyi.web',
'action':'FY_BY_REALTlME',
}
print(str(int(time.time()*1000)))

print(json.dumps(data))
print('' if '' else (5,))