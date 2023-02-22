ArmCountsPerRev = 28
ArmGearRatio = (32.0/10.0) * (76.0/21.0) * (68.0/13.0)
ArmCountsPerDegree = ArmCountsPerRev * ArmGearRatio /360

print(ArmCountsPerDegree*(1/238))
print(ArmCountsPerDegree*(1/802))