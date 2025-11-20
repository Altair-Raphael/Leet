class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        frequencia = {}
        
        
        for num in nums:
            if num in frequencia :
                frequencia [num] += 1
            else:
                frequencia [num] = 1
            
        resposta = []
        
        for chave in frequencia:
            if frequencia[chave] == 1:
                resposta.append(chave)
                 
        return resposta