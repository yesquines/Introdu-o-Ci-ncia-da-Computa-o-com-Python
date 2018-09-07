def menor_nome(nomes):
  
	menornomej = ""
  
	menornome = ""
  
	for i in range(0, len(nomes)):
    
		for j in range(0, len(nomes)):
      
			if len(nomes[i].strip()) < len(nomes[j].strip()):
        
				if nomes[i].strip() != menornomej:
          
					menornomej = nomes[i].strip()
      
				else:
        
					if len(nomes[i].strip()) == len(nomes[j].strip()):
          
						if i < j:
            
							menornomej = nomes[i].strip()
          
						else:
							menornomej = nomes[j].strip()
       
					else:
          
						if nomes[j].strip() != menornomej:

							menornomej = nomes[j].strip()

		if len(menornome) == 0:
      
			menornome = menornomej;   
		else: 
      
			if len(menornome) > len(menornomej):
        
				menornome = menornomej
	menornome = menornome.capitalize()
  
	return menornome