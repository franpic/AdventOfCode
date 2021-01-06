if __name__ == "__main__":
    data = (
        1337,
        1906,
        2007,
        1939,
        818,
        1556,
        2005,
        1722,
        1484,
        1381,
        1682,
        1253,
        1967,
        1718,
        2002,
        1398,
        1439,
        1689,
        1746,
        1979,
        1985,
        1387,
        1509,
        1566,
        1276,
        1625,
        1853,
        882,
        1750,
        1390,
        1731,
        1555,
        1860,
        1675,
        1457,
        1554,
        1506,
        1639,
        1543,
        1849,
        1062,
        1869,
        1769,
        1858,
        1916,
        1504,
        1747,
        1925,
        1275,
        1273,
        1383,
        1816,
        1814,
        1481,
        1649,
        1993,
        1759,
        1949,
        1499,
        1374,
        1613,
        1424,
        783,
        1765,
        1576,
        1933,
        1270,
        1844,
        1856,
        1634,
        1261,
        1293,
        1741,
        668,
        1573,
        1599,
        1877,
        1474,
        1918,
        476,
        1515,
        1029,
        202,
        1589,
        1867,
        1503,
        1582,
        1605,
        1557,
        587,
        1462,
        1955,
        1806,
        1834,
        1739,
        1343,
        1594,
        1622,
        1972,
        1527,
        1798,
        1719,
        1866,
        134,
        2000,
        1992,
        1966,
        1909,
        1340,
        1621,
        1921,
        1256,
        1365,
        1314,
        1748,
        1963,
        1379,
        1627,
        1848,
        1977,
        1917,
        1826,
        1716,
        1631,
        1404,
        1936,
        1677,
        1661,
        1986,
        1997,
        1603,
        1932,
        1780,
        1902,
        2009,
        1257,
        1871,
        1362,
        1662,
        1507,
        1255,
        1539,
        1962,
        1886,
        1513,
        1264,
        1873,
        1700,
        807,
        1426,
        1697,
        1698,
        1519,
        1791,
        1240,
        1542,
        1497,
        1761,
        1640,
        1502,
        1770,
        1437,
        1333,
        1805,
        1591,
        1644,
        1420,
        1809,
        1587,
        1421,
        1540,
        1942,
        470,
        1940,
        1831,
        1247,
        1632,
        1975,
        1774,
        1919,
        1829,
        1944,
        1553,
        1361,
        1483,
        1995,
        1868,
        1601,
        1552,
        1854,
        1490,
        1855,
        1987,
        1538,
        1389,
        1454,
        1427,
        1686,
        1456,
        1974,
    )

    print(
        tuple(
            (a, b, c, a * b * c)
            for a in data for b in data for c in data
            if a + b + c == 2020))
