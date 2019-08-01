import re

data = """
<table>
<tr>
    <td>One</td>
    <td>Two</td>
</tr>
</table>
"""
import re               
lst = re.findall("<.*?>(.*)</.*?>",data)
print(lst)


emails = """krishna.t@wipro.com
lakshman.a@spaneos.com
lakshman.a@heraizen.edu"""
lst1=re.findall("@([a-z]+).",emails)
print(lst1)

