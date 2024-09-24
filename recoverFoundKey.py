def recoverFoundKey(result, privateKey1):
    half = 57896044618658097711785492504343953926418782139537452191302581570759080747169
    N = 115792089237316195423570985008687907852837564279074904382605163141518161494337
    third = 77194726158210796949047323339125271901891709519383269588403442094345440996225
    twosResult = result[1][0]
    threesResult = result[1][1]
    if twosResult >= 0 and threesResult >= 0:
        foundPrivateKey = (privateKey1 * (((half ** twosResult)*(third ** threesResult))%N))%N
        return(foundPrivateKey)
    elif twosResult < 0 and threesResult >= 0:
        twosResult = 0 - twosResult
        foundPrivateKey = (privateKey1 * (((2 ** twosResult)*(third ** threesResult))%N))%N
        return(foundPrivateKey)
    elif twosResult >= 0 and threesResult < 0:
        threesResult = 0 - threesResult
        foundPrivateKey = (privateKey1 * (((half ** twosResult)*(3 ** threesResult))%N))%N
        return(foundPrivateKey)
    elif twosResult < 0 and threesResult < 0:
        twosResult = 0 - twosResult
        threesResult = 0 - threesResult
        foundPrivateKey = (privateKey1 * (((2 ** twosResult)*(3 ** threesResult))%N))%N
        return(foundPrivateKey)