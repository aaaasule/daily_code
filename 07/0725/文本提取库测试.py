# -*- coding:utf-8 -*-
from cocoNLP.extractor import extractor

ex = extractor()

text = "1937年，八路军115师在平型关大捷之后，根据中共中央部署，一部3000人由政委聂荣臻率领转战至晋东北地区。11月7日，即太原被日寇攻陷的前一天，聂荣臻等在五台山成立了晋察冀军区，创建了全国第一个敌后抗日根据地。11月18日，在日寇的“围剿”中，晋察冀军区领导机关转移至太行山深处河北阜平县城。为宣传组织全民抗战，鼓舞边区军民抗日斗志，聂荣臻和中共晋察冀省委书记黄敬、军区政治部主任舒同等，共同商定创办一份晋察冀全区性党报"

resp_location = ex.extract_locations(text)

print(resp_location)