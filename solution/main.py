import tests_generator
import matplotlib.pyplot as plt
import sys
from recursive_parser import solve
from tests_generator import get_time_data


#solve(sys.argv[1])
data = tests_generator.get_time_data()
#data = [(12698, 237.4), (61801, 736.4), (51143, 938.2), (53889, 420.8), (71078, 700.6), (49027, 457.4), (54131, 390.8), (58565, 509.0), (38202, 412.0), (28433, 236.8), (248645, 2359.8), (104589, 883.8), (375091, 3114.6), (133910, 1169.8), (301030, 2537.6), (244011, 2463.6), (343066, 2453.8), (111855, 1087.0), (199888, 1644.6), (337631, 3620.8), (242995, 1903.4), (340628, 2681.0), (359305, 2957.0), (369511, 3197.2), (382401, 3938.8), (1469947, 10992.0), (1041158, 7787.8), (1459721, 17278.2), (290734, 2173.0), (1518747, 12000.8), (1166217, 10086.6), (1186513, 9807.6), (924637, 7618.4), (871530, 6709.6), (905761, 9347.4), (873117, 98561.8), (991203, 9057.4), (1139472, 10444.2), (1547392, 12136.6), (565028, 4976.6), (770793, 6344.8), (1177412, 11216.4), (1338998, 87333.8), (247194, 2215.4), (1368501, 10857.8), (606963, 4942.0), (1467251, 11626.6), (1141336, 9834.2), (6299050, 61643.4), (1217815, 12954.0), (3310814, 32516.2), (1669195, 24442.6), (6355043, 78393.0), (3367134, 58010.4), (3650960, 34934.0), (5569249, 58145.8), (5482182, 58984.6), (924678, 11598.4), (4622577, 39272.2), (3634513, 31702.6), (3154867, 27532.8), (888035, 12573.6), (3962987, 48339.2), (2396331, 31190.2), (5371358, 47661.0), (3478120, 34434.4), (4871112, 76558.2), (2838068, 53035.6), (2198288, 29959.8), (6299660, 101640.2), (858697, 9745.8), (1484780, 17967.8), (3077728, 63698.8), (4562718, 48562.8), (665422, 6676.2), (1300684, 13582.8), (1716043, 17660.8), (4140282, 51300.0), (6066735, 73589.8), (4795554, 66940.0)]

print(data)
x_data = [elem[0] for elem in data]
y_data = [elem[1] for elem in data]

plt.scatter(x_data, y_data)
plt.show()
