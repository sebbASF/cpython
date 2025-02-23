#!/usr/bin/env python3

# Show that msg.as_bytes() is not consistent across Python versions

import email
import email.policy
import hashlib

class DataEntry:
    def __init__(self, name: str, datalen: int, datahash: str, byteslen: int, byteshash: str):
        self.name = name
        self.datalen = datalen
        self.datahash = datahash
        self.byteslen = byteslen
        self.byteshash = byteshash

TEST_DATA = [
    DataEntry('msg_01.txt', 459, '0d7379681894151742e00504e7ca8796', 459, '0d7379681894151742e00504e7ca8796'),
    DataEntry('msg_02.txt', 2812, 'fde67c346d38a0f98d83f9c9357df9a6', 2812, 'fde67c346d38a0f98d83f9c9357df9a6'),
    DataEntry('msg_03.txt', 366, '46413e3ecbdb0124636aa16b0d8b3ea6', 366, '46413e3ecbdb0124636aa16b0d8b3ea6'),
    DataEntry('msg_04.txt', 961, '7421268a46f72276de6b015b393a3577', 961, '7421268a46f72276de6b015b393a3577'),
    DataEntry('msg_05.txt', 558, '0e05fa635ef13e72c6ef864f69a3a913', 558, '0e05fa635ef13e72c6ef864f69a3a913'),
    DataEntry('msg_06.txt', 1041, '99412fc04181031556cb9c96863b8caa', 1041, '99412fc04181031556cb9c96863b8caa'),
    DataEntry('msg_07.txt', 5227, 'beb3d7cfa4d5b77be8b37d1c433539c4', 5227, 'beb3d7cfa4d5b77be8b37d1c433539c4'),
    DataEntry('msg_08.txt', 454, 'fb0e8a1f8da7a434d80f12dd318ace88', 454, 'fb0e8a1f8da7a434d80f12dd318ace88'),
    DataEntry('msg_09.txt', 432, '306ecab54f1bd6be39b608f730032e02', 432, '306ecab54f1bd6be39b608f730032e02'),
    DataEntry('msg_10.txt', 884, 'f78f0c171498993b3a5e2392b3cf35b9', 884, 'f78f0c171498993b3a5e2392b3cf35b9'),
    DataEntry('msg_11.txt', 142, '8b63eb1798f9072fb42409869edafe1e', 142, '8b63eb1798f9072fb42409869edafe1e'),
    DataEntry('msg_12.txt', 644, '6c4183207d1cf66e83ffc671cb28dda4', 645, '3a2feb4a4cfcf5d153500eda595629f2'),
    DataEntry('msg_13.txt', 5367, 'e40c7ddf7dcba1c655445f7899e977e8', 5367, 'e40c7ddf7dcba1c655445f7899e977e8'),
    DataEntry('msg_14.txt', 641, '76df79a3f3e66c19b77e69205d9ffb72', 641, '76df79a3f3e66c19b77e69205d9ffb72'),
    DataEntry('msg_15.txt', 1306, 'aa138693fca83e045cc5f523bee6b2e2', 1307, 'c51a13a044732df972fddb16fb956f06'),
    DataEntry('msg_16.txt', 5203, '197aac66100ffb774044fe42a72b11fd', 5203, '197aac66100ffb774044fe42a72b11fd'),
    DataEntry('msg_17.txt', 330, 'd4f9e1edd242a0c5a3b34cbe97ebdabe', 330, 'd4f9e1edd242a0c5a3b34cbe97ebdabe'),
    DataEntry('msg_18.txt', 230, '1fc6b08d9aeaa7902a069c1bf1d9dd5e', 230, '1fc6b08d9aeaa7902a069c1bf1d9dd5e'),
    DataEntry('msg_19.txt', 757, 'fbba32714b398097aaa061975eddc42b', 758, 'ff1a2b3708156ab4f8ff1f0d54188831'),
    DataEntry('msg_20.txt', 507, 'abf4778b3c1eca76b1819c51c954de80', 507, 'abf4778b3c1eca76b1819c51c954de80'),
    DataEntry('msg_21.txt', 376, '5e165ce977b0894106a802a1c2701b17', 376, '5e165ce977b0894106a802a1c2701b17'),
    DataEntry('msg_22.txt', 1894, '4d452dc300b431813481e8721760e6ec', 1894, '4d452dc300b431813481e8721760e6ec'),
    DataEntry('msg_23.txt', 139, 'db0e7bf714679a813462266f226f6c21', 139, 'db0e7bf714679a813462266f226f6c21'),
    DataEntry('msg_24.txt', 157, 'de3d2c04b4dfd5413c28e0a1e9164526', 157, 'de3d2c04b4dfd5413c28e0a1e9164526'),
    DataEntry('msg_25.txt', 5122, 'b3310f3c4ab013eff4b0c956f242ab57', 5078, '26903aed4cd67ada61bd3da69447f1e4'),
    DataEntry('msg_26.txt', 2103, '93fdd6045c0b5e293d7495b58c5f1ef3', 2057, '9d7f414dfceaa7dedf3aaacd44f6b471'),
    DataEntry('msg_27.txt', 578, 'ecf907082425783fe2a94ac5b787f5ff', 578, 'ecf907082425783fe2a94ac5b787f5ff'),
    DataEntry('msg_28.txt', 380, 'b489861f9c2aa89ae3e44b0d8782d49b', 380, 'b489861f9c2aa89ae3e44b0d8782d49b'),
    DataEntry('msg_29.txt', 583, 'd333dad6440b4df4978207a0308e2c72', 583, 'd333dad6440b4df4978207a0308e2c72'),
    DataEntry('msg_30.txt', 322, '524238f232f74c03700e03ad8f92e6f3', 322, '524238f232f74c03700e03ad8f92e6f3'),
    DataEntry('msg_31.txt', 200, 'af049868db1235193d6f4d4dc9b4f9c4', 200, 'af049868db1235193d6f4d4dc9b4f9c4'),
    DataEntry('msg_32.txt', 418, 'd89a98399941e974920032491cd69886', 418, 'd89a98399941e974920032491cd69886'),
    DataEntry('msg_33.txt', 750, '8170e05c633da34cd445541be5ae53de', 750, '8170e05c633da34cd445541be5ae53de'),
    DataEntry('msg_34.txt', 300, '924961579f14d1d54257745c7042e8ef', 300, '924961579f14d1d54257745c7042e8ef'),
    DataEntry('msg_35.txt', 136, 'bc81d0f30d8c07e9201354c6ea2dbdbd', 137, 'b47618871105553e971b254fa11c8ed9'),
    DataEntry('msg_36.txt', 816, '290c6739a56ae65e542c8781cd79ebe6', 816, '290c6739a56ae65e542c8781cd79ebe6'),
    DataEntry('msg_37.txt', 209, 'f56f272721a1cfdb0e86d6d3e0827ce2', 177, 'd637faa222ad797c51420cc023c111a8'),
    DataEntry('msg_38.txt', 2548, 'cec2ae10906e99dd30eb09c65ffb0af3', 2598, '662cff0e0a0723b89cb3978ced8eb9eb'),
    DataEntry('msg_39.txt', 1955, 'd9dde09eed5a496788688f0652a96cfb', 1956, 'aa241c21bc131cb1ba1134dbff8314d6'),
    DataEntry('msg_40.txt', 197, '27e880e1fbf80075ff676b76cac6df50', 197, '27e880e1fbf80075ff676b76cac6df50'),
    DataEntry('msg_41.txt', 185, '1111f57890bc01c3384752e0e37ce55c', 185, '1111f57890bc01c3384752e0e37ce55c'),
    DataEntry('msg_42.txt', 313, 'e316bd8ce0b291cd97997bd0ad6ce2f1', 305, 'f7a22bf998f315de4a5fd4391e2788cc'),
    DataEntry('msg_43.txt', 9166, '93992f3bebc941e5c45a95ffb6a29799', 9084, '7bbbd72943d7c28a29d7c12f97a102f8'),
    DataEntry('msg_44.txt', 895, 'eadd8b8b81a7f600a4dfb74e2af80df0', 895, 'eadd8b8b81a7f600a4dfb74e2af80df0'),
    DataEntry('msg_45.txt', 965, '0dc555b1792a3599b3236527fd96f5dd', 965, '0dc555b1792a3599b3236527fd96f5dd'),
    DataEntry('msg_46.txt', 816, '748de2ed8d11473c03e05ed3acf871fc', 816, '748de2ed8d11473c03e05ed3acf871fc'),
    DataEntry('msg_47.txt', 232, '8bafae7751f742a9e5cc83c75d281469', 235, '378c4100251c58f7929bfb65d7134b4b'),
    DataEntry('msg_50.txt', 545, 'd4b1d7a882266e5c28a2e1a376ab5b61', 545, 'd4b1d7a882266e5c28a2e1a376ab5b61'),
    DataEntry('msg_51.txt', 551, 'eddd5f1ac04f16a9e6c0d7452ff8c4d1', 551, 'eddd5f1ac04f16a9e6c0d7452ff8c4d1'),
    DataEntry('msg_52.txt', 546, '7d20cf09c7fcbfcb8abf928521a93165', 546, '7d20cf09c7fcbfcb8abf928521a93165'),
    DataEntry('msg_53.txt', 586, 'a887d9480e5318313f7d86abb1005d24', 586, 'a887d9480e5318313f7d86abb1005d24'),
]

DATA_SOURCE = 'Lib/test/test_email/data'

def testmsg(filename):
    policy = email.policy.default.clone(refold_source='none')
    with open(f"{DATA_SOURCE}/{filename}", 'rb') as fp:
        data = fp.read()
    ldata = len(data)
    hdata = hashlib.md5(data).hexdigest()
    msg = email.message_from_bytes(data, policy=policy)
    asbytes = msg.as_bytes()
    lbytes = len(asbytes)
    hbytes = hashlib.md5(asbytes).hexdigest()
    return [ldata, hdata, lbytes, hbytes, data, asbytes]

def main():
    print('Start')
    errors = 0
    for e in TEST_DATA:
        ldata, hdata, lbytes, hbytes, data, asbytes = testmsg(e.name)
        # This is fatal
        assert ldata == e.datalen and hdata == e.datahash, \
            f"Bad input data: expected: {e.datalen} {e.datahash}, actual: {ldata} {hdata}"
        if lbytes != e.byteslen or hbytes != e.byteshash: # fail at end
            print(f"{e.name}: Bad output data, expected: {e.byteslen} {e.byteshash}, actual: {lbytes} {hbytes}")
            errors += 1
            ds = data.split(b'\n')
            bs = asbytes.split(b'\n')
            for idx,x in enumerate(ds):
                if x != bs[idx]:
                    print(idx,x)
                    print(idx,bs[idx])
                    break
    assert errors == 0, f"Errors detected: {errors}"
    print('Done')

if __name__ == '__main__':
    main()
