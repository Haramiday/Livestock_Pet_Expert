from django.shortcuts import render
from experta import *
from .models import GoatSym,GoatDisInfo,CowSym,CowDisInfo,ChickenSym,ChickenDisInfo,DogSym,DogDisInfo,CatSym,CatDisInfo,AnimalInfo,Prescription
from pathlib import Path
import os
import operator
# Create your views here.


#certainty factor
def cf_symptom(old, nex):
	return old + (nex*(1-old))

def certainty(animal,user_input):
	directory = os.path.dirname(__file__)+"/"+animal
	mother_dir = Path(directory)
	list_filepath = list(mother_dir.glob('*.txt'))

	final_cf = {}

	for ind in range(len(list_filepath)):
		filepath = list_filepath[ind]
		filename = list_filepath[ind].name[:-4]
		file = open(filepath,'r')
		content = file.readlines()
		#print(content)

		disease = {}
		disease[filename]={}
		for i in content:
			#print(i.split(','))
			split = i.split(',')
			#print(split)
			disease[filename][split[0]] = float(split[1])
		#print(disease) 

		print(filename)
		for sym in disease[filename]:
			print('symptom: ',sym)
			
			disease[filename][sym] = disease[filename][sym] * float(user_input[sym])

		#print(disease) 

		cf = list(disease[filename].values())
		#print(cf)



		old = cf[0]
		for i in range(1,len(cf)):
			nex = cf[i] 
			old = cf_symptom(old,nex)
			#print(old)
		final_cf[filename] = old
	print(final_cf)
	#print({k: v for k, v in sorted(final_cf.items(), key=lambda item: item[1])})

	sorted_d = dict( sorted(final_cf.items(), key=operator.itemgetter(1),reverse=True))
	#print('Dictionary in descending order by value : ',sorted_d)
	if sorted_d[list(sorted_d.keys())[0]] == 0:
		message = 'none'
	elif sorted_d[list(sorted_d.keys())[0]] >= 0.5:
		message = "The most probable disease that is "+list(sorted_d.keys())[0]
		
	else:
		message = "We couldn't diagnose the disease, but it is looking like "+list(sorted_d.keys())[0]
	return message,list(sorted_d.keys())[0],sorted_d



#HOME
def home(request):

	return render(request,"index.html",{})

#GOAT
def goatexpert(sympList):
	class Goat(Fact):
		pass

	class GoatDisease(KnowledgeEngine):
		def __init__(self):
			KnowledgeEngine.__init__(self)
		@Rule(Goat(disease='fever') | Goat(disease='bloody discharge') | Goat(disease='sudden death'))
		def is_anthrax(self,disease='Anthrax'):
			self.disease = disease
			
		@Rule(Goat(disease='swelling of lower mandible')| Goat(disease='diarrhea')|Goat(disease='fever')|Goat(disease='dysentery'))
		def is_haemorrhagic(self,disease='Haemorrhagic Septicemia'):
			self.disease = disease
			
		@Rule(Goat(disease='abortion during late pregnancy')| Goat(disease='scrotal swelling in male')| Goat(disease='reduced milk production') | Goat(disease='infertility')| Goat(disease='joint swelling')| Goat(disease='birth of weak offspring'))
		def is_brucellosis(self,disease='Brucellosis'):
			self.disease = disease
			
		@Rule(Goat(disease='mucous diarrhea')| Goat(disease='sudden death'))
		def is_enterotoxaemia(self,disease='Enterotoxaemia'):
			self.disease = disease
			
		@Rule(Goat(disease='cough')| Goat(disease='mucous discharge from nostril')| Goat(disease='respiratory distress')| Goat(disease='reduced feed intake') | Goat(disease='fever'))
		def is_pneumonia(self,disease='Pneumonia'):
			self.disease = disease
			
		@Rule(Goat(disease='foot wound'))
		def is_footrot(self,disease='Foot rot'):
			self.disease = disease

		@Rule(Goat(disease='udder swelling')| Goat(disease='milk change'))
		def is_mastitis(self,disease='Mastitis'):
			self.disease = disease
			
		@Rule(Goat(disease='fever')| Goat(disease='O&N mucous')| Goat(disease='respiratory distress')| Goat(disease='wound'))
		def is_ppr(self,disease='Peste Des Petits Ruminants'):
			self.disease = disease
			
		@Rule(Goat(disease='difficult in walking')| Goat(disease='excess salivary secretion')| Goat(disease='wound')| Goat(disease='fever'))
		def is_fmd(self,disease='Foot and Mouth Disease'):
			self.disease = disease
			
		@Rule(Goat(disease='pox lesion')| Goat(disease='fever')| Goat(disease='O&N mucous')| Goat(disease='respiratory distress'))
		def is_goatpox(self,disease='Goat Pox'):
			self.disease = disease
			
		@Rule(Goat(disease='emaciation')| Goat(disease='anaemia')| Goat(disease='edema'))
		def is_fluke(self,disease='Fluke infection'):
			self.disease = disease
			
		@Rule(Goat(disease='fever')| Goat(disease='reduced growth')| Goat(disease='kid mortality'))
		def is_tape(self,disease='Tape worm'):
			self.disease = disease
			
		@Rule(Goat(disease='fever')| Goat(disease='reduced growth')| Goat(disease='anaemia')| Goat(disease='edema'))
		def is_round(self,disease='Round worm'):
			self.disease = disease
			
		@Rule(Goat(disease='brownish diarrhea')| Goat(disease='anaemia')| Goat(disease='kid mortality'))
		def is_coccidiosis(self,disease='Coccidiosis'):
			self.disease = disease
			
		@Rule(Goat(disease='skin allergy')| Goat(disease='reduced growth')| Goat(disease='wound'))
		def is_tick(self,disease='Tick and lice'):
			self.disease = disease
			

	if len(sympList) ==1:
		engine = GoatDisease()
		engine.reset()
		engine.declare(Goat(disease=sympList[0]))
		# engine.run()
		# print(dir(engine))
		# print(engine.disease)
		return engine
	elif len(sympList) ==2:
		engine = GoatDisease()
		engine.reset()
		engine.declare(Goat(disease=sympList[0]),Goat(disease=sympList[1]))
		return engine
	elif len(sympList) ==3:
		engine = GoatDisease()
		engine.reset()
		engine.declare(Goat(disease=sympList[0]),Goat(disease=sympList[1]),Goat(disease=sympList[2]))
		return engine
	elif len(sympList) ==4:
		engine = GoatDisease()
		engine.reset()
		engine.declare(Goat(disease=sympList[0]),Goat(disease=sympList[1]),Goat(disease=sympList[2]),Goat(disease=sympList[3]))
		return engine
	elif len(sympList) ==5:
		engine = GoatDisease()
		engine.reset()
		engine.declare(Goat(disease=sympList[0]),Goat(disease=sympList[1]),Goat(disease=sympList[2]),Goat(disease=sympList[3]),Goat(disease=sympList[4]))
		return engine
	elif len(sympList) ==6:
		engine = GoatDisease()
		engine.reset()
		engine.declare(Goat(disease=sympList[0]),Goat(disease=sympList[1]),Goat(disease=sympList[2]),Goat(disease=sympList[3]),Goat(disease=sympList[4]),Goat(disease=sympList[5]))
		return engine
	elif len(sympList) ==7:
		engine = GoatDisease()
		engine.reset()
		engine.declare(Goat(disease=sympList[0]),Goat(disease=sympList[1]),Goat(disease=sympList[2]),Goat(disease=sympList[3]),Goat(disease=sympList[4]),Goat(disease=sympList[5]),Goat(disease=sympList[6]))
		return engine
	elif len(sympList) ==8:
		engine = GoatDisease()
		engine.reset()
		engine.declare(Goat(disease=sympList[0]),Goat(disease=sympList[1]),Goat(disease=sympList[2]),Goat(disease=sympList[3]),Goat(disease=sympList[4]),Goat(disease=sympList[5]),Goat(disease=sympList[6]),Goat(disease=sympList[7]))
		return engine
	elif len(sympList) ==9:
		engine = GoatDisease()
		engine.reset()
		engine.declare(Goat(disease=sympList[0]),Goat(disease=sympList[1]),Goat(disease=sympList[2]),Goat(disease=sympList[3]),Goat(disease=sympList[4]),Goat(disease=sympList[5]),Goat(disease=sympList[6]),Goat(disease=sympList[7]),Goat(disease=sympList[8]))
		return engine
	elif len(sympList) ==10:
		engine = GoatDisease()
		engine.reset()
		engine.declare(Goat(disease=sympList[0]),Goat(disease=sympList[1]),Goat(disease=sympList[2]),Goat(disease=sympList[3]),Goat(disease=sympList[4]),Goat(disease=sympList[5]),Goat(disease=sympList[6]),Goat(disease=sympList[7]),Goat(disease=sympList[8]),Goat(disease=sympList[9]))
		return engine


# def ask_goat(request):
# 	if request.method == "POST":
# 		n = request.POST.getlist('symptom')
# 		print('RESULT:',n)
# 		print(len(n))
# 		l=goatexpert(n)
# 		l.run()
# 		print(l.disease)

# 		#Query the database
# 		list_of_symptoms = [i.symptom for i in GoatSym.objects.all()]
# 		dis_info = GoatDisInfo.objects.filter(disease = l.disease) 
# 		prescription_info = Prescription.objects.filter(disease = l.disease) 
# 		list_sym = [GoatSym.objects.filter(symptom = i)[0] for i in dis_info[0].sym.split(',') if i in list_of_symptoms]
# 		print(list_sym)
# 		print(dis_info)
# 		if len(prescription_info)>0:
# 			prescription = prescription_info[0].prescription
# 		else:
# 			prescription = ''
# 		return render(request,"result.html",{'info':dis_info[0],'symptoms':list_sym,'prescription':prescription})

# 	return render(request,"goat_form.html",{})


def ask_goat(request):
	if request.method == "POST":
		n = request.POST.getlist('symptom')
		print('RESULT:',n)
		s = ['fever', 'bloody discharge', 'dysentry', 'swelling of lower mandible', 'abortion during late pregnancy', 'infertility', 'scrotal swelling in male', 'joint swelling', 'mucous diarrhea', 'respiratory distress', 'mucous discharge from nostril', 'reduced feed intake', 'weight gain', 'cough', 'foot wound', 'udder swelling', 'milk change', 'O&N mucous', 'brownish diarrhea', 'excess salivary secretion', 'difficult in walking', 'pox lesion', 'anaemia', 'reduced growth', 'edema', 'kid mortality', 'skin allergy', 'wound', 'sudden death', 'emaciation', 'diarrhea']
		print('check: ',len(n)==len(s))
		res = dict(zip(s, n))
		print(res)
		
		message,dis,table = certainty("goat",res)
		if message == 'none':
			return render(request,"goat_form.html",{})
		else:
			#Query the database
			list_of_symptoms = [i.symptom for i in GoatSym.objects.all()]
			dis_info = GoatDisInfo.objects.filter(disease = dis) 
			prescription_info = Prescription.objects.filter(disease = dis) 
			list_sym = [GoatSym.objects.filter(symptom = i)[0] for i in dis_info[0].sym.split(',') if i in list_of_symptoms]
			print(list_sym)
			print(dis_info)
			if len(prescription_info)>0:
				prescription = prescription_info[0].prescription
			else:
				prescription = ''
			return render(request,"result.html",{'info':dis_info[0],'symptoms':list_sym,'prescription':prescription,"message":message,'table':table})

	return render(request,"goat_form.html",{})



#CHICKEN
def chickenexpert(sympList):
	class Chicken(Fact):
		pass

	class ChickenDisease(KnowledgeEngine):
		def __init__(self):
			KnowledgeEngine.__init__(self)
		@Rule(OR(Chicken(disease='open beak'),Chicken(disease='ruffled feather'),Chicken(disease='swollen comb and wattle'),Chicken(disease='yellowish diarrhoea'),Chicken(disease='loss of appetite')))
		def is_fowlcholera(self,disease='Fowl cholera'):
			self.disease = disease
			
		@Rule(Chicken(disease='Reduction in egg production')|Chicken(disease='Reduction in fertility')|Chicken(disease='Reduction in hatchability')|Chicken(disease='greenish faeces')|Chicken(disease='weakness'))
		def is_fowltyphoid(self,disease='Fowl typhoid'):
			self.disease = disease
			
		@Rule(Chicken(disease='conjunctivitis with closed eye')|Chicken(disease='nasal and occular discharges')|Chicken(disease='facial oedema'))
		def is_coryza(self,disease='Infectious coryza'):
			self.disease = disease
			
		@Rule(Chicken(disease='coughing')|Chicken(disease='sneezing')|Chicken(disease='Nasal discharge')|Chicken(disease='shaking of head')|Chicken(disease='Loss of weight')|Chicken(disease='Reduction in egg production')|Chicken(disease='Reduction in fertility'))
		def is_chronic(self,disease='Chronic respiratory disease'):
			self.disease = disease
			
		@Rule(Chicken(disease='gasping')|Chicken(disease='coughing')|Chicken(disease='sneezing')|Chicken(disease='Nasal discharge')|Chicken(disease='respiratory distress'))
		def is_avianinfectious(self,disease='Avian infectious bronchitis'):
			self.disease = disease
			
		@Rule(Chicken(disease='difficulty breathing')|Chicken(disease='paralysis')|Chicken(disease='blindness')|Chicken(disease='death'))
		def is_md(self,disease='Mareks disease'):
			self.disease = disease
			
		@Rule(Chicken(disease='greenish faeces')|Chicken(disease='twisting of head and neck')|Chicken(disease='sneezing')|Chicken(disease='Nasal discharge')|Chicken(disease='respiratory distress'))
		def is_nd(self,disease='Newcastle disease'):
			self.disease = disease
			
		@Rule(Chicken(disease='weakness or depression')|Chicken(disease='white diarrhea')|Chicken(disease='cluster near heat sources'))
		def is_pd(self,disease='Pullorum disease'):
			self.disease = disease
			
		
			

	if len(sympList) ==1:
		engine = ChickenDisease()
		engine.reset()
		engine.declare(Chicken(disease=sympList[0]))
		return engine
	elif len(sympList) ==2:
		engine = ChickenDisease()
		engine.reset()
		engine.declare(Chicken(disease=sympList[0]),Chicken(disease=sympList[1]))
		return engine
	elif len(sympList) ==3:
		engine = ChickenDisease()
		engine.reset()
		engine.declare(Chicken(disease=sympList[0]),Chicken(disease=sympList[1]),Chicken(disease=sympList[2]))
		return engine
	elif len(sympList) ==4:
		engine = ChickenDisease()
		engine.reset()
		engine.declare(Chicken(disease=sympList[0]),Chicken(disease=sympList[1]),Chicken(disease=sympList[2]),Chicken(disease=sympList[3]))
		return engine
	elif len(sympList) ==5:
		engine = ChickenDisease()
		engine.reset()
		engine.declare(Chicken(disease=sympList[0]),Chicken(disease=sympList[1]),Chicken(disease=sympList[2]),Chicken(disease=sympList[3]),Chicken(disease=sympList[4]))
		return engine
	elif len(sympList) ==6:
		engine = ChickenDisease()
		engine.reset()
		engine.declare(Chicken(disease=sympList[0]),Chicken(disease=sympList[1]),Chicken(disease=sympList[2]),Chicken(disease=sympList[3]),Chicken(disease=sympList[4]),Chicken(disease=sympList[5]))
		return engine
	elif len(sympList) ==7:
		engine = ChickenDisease()
		engine.reset()
		engine.declare(Chicken(disease=sympList[0]),Chicken(disease=sympList[1]),Chicken(disease=sympList[2]),Chicken(disease=sympList[3]),Chicken(disease=sympList[4]),Chicken(disease=sympList[5]),Chicken(disease=sympList[6]))
		return engine
	elif len(sympList) ==8:
		engine = ChickenDisease()
		engine.reset()
		engine.declare(Chicken(disease=sympList[0]),Chicken(disease=sympList[1]),Chicken(disease=sympList[2]),Chicken(disease=sympList[3]),Chicken(disease=sympList[4]),Chicken(disease=sympList[5]),Chicken(disease=sympList[6]),Chicken(disease=sympList[7]))
		return engine
	elif len(sympList) ==9:
		engine = ChickenDisease()
		engine.reset()
		engine.declare(Chicken(disease=sympList[0]),Chicken(disease=sympList[1]),Chicken(disease=sympList[2]),Chicken(disease=sympList[3]),Chicken(disease=sympList[4]),Chicken(disease=sympList[5]),Chicken(disease=sympList[6]),Chicken(disease=sympList[7]),Chicken(disease=sympList[8]))
		return engine
	elif len(sympList) ==10:
		engine = ChickenDisease()
		engine.reset()
		engine.declare(Chicken(disease=sympList[0]),Chicken(disease=sympList[1]),Chicken(disease=sympList[2]),Chicken(disease=sympList[3]),Chicken(disease=sympList[4]),Chicken(disease=sympList[5]),Chicken(disease=sympList[6]),Chicken(disease=sympList[7]),Chicken(disease=sympList[8]),Chicken(disease=sympList[9]))
		return engine


# def ask_chicken(request):
# 	if request.method == "POST":
# 		n = request.POST.getlist('symptom')
# 		print(len(n))
# 		l=chickenexpert(n)
# 		l.run()
# 		print('disease: ',l.disease)

# 		list_of_symptoms = [i.symptom for i in ChickenSym.objects.all()]
# 		print('list_of_symptoms: ',list_of_symptoms)
# 		dis_info = ChickenDisInfo.objects.filter(disease = l.disease) 
# 		print("info: ", [i.disease for i in ChickenDisInfo.objects.all()])
# 		print('dis_info: ',dis_info)
# 		list_sym = [ChickenSym.objects.filter(symptom = i)[0] for i in dis_info[0].sym.split(',') if i in list_of_symptoms]
# 		print(list_sym)
# 		print(dis_info)
# 		prescription_info = Prescription.objects.filter(disease = l.disease) 
# 		if len(prescription_info)>0:
# 			prescription = prescription_info[0].prescription
# 		else:
# 			prescription = ''
# 		return render(request,"result.html",{'info':dis_info[0],'symptoms':list_sym,'prescription':prescription})

# 	return render(request,"chicken_form.html",{})


def ask_chicken(request):
	if request.method == "POST":
		n = request.POST.getlist('symptom')
		print(len(n))
		s = ['open beak', 'ruffled feather', 'swollen comb and wattle', 'yellowish diarrhoea', 'Reduction in egg production', 'Reduction in fertility', 'Reduction in hatchability', 'greenish faeces', 'conjunctivitis with closed eye', 'nasal and occular discharges', 'facial oedema', 'Nasal discharge', 'shaking of head', 'coughing', 'loss of weight', 'gasping', 'respiratory distress', 'sneezing', 'difficulty breathing', 'death', 'blindness', 'paralysis', 'twisting of head and neck', 'weakness', 'white diarrhea', 'cluster near heat sources', 'loss of appetite']
		print(n)
		print('check: ',len(n)==len(s))
		res = dict(zip(s, n))
		print(res)
		
		message,dis,table = certainty("chicken",res)
		if message == 'none':
			return render(request,"chicken_form.html",{})
		else:
			list_of_symptoms = [i.symptom for i in ChickenSym.objects.all()]
			print('list_of_symptoms: ',list_of_symptoms)
			dis_info = ChickenDisInfo.objects.filter(disease = dis) 
			print("info: ", [i.disease for i in ChickenDisInfo.objects.all()])
			print('dis_info: ',dis_info)
			list_sym = [ChickenSym.objects.filter(symptom = i)[0] for i in dis_info[0].sym.split(',') if i in list_of_symptoms]
			print(list_sym)
			print(dis_info)
			prescription_info = Prescription.objects.filter(disease = dis) 
			if len(prescription_info)>0:
				prescription = prescription_info[0].prescription
			else:
				prescription = ''
			return render(request,"result.html",{'info':dis_info[0],'symptoms':list_sym,'prescription':prescription,'message':message,'table':table})

	return render(request,"chicken_form.html",{})




#CATTLE
def cowexpert(sympList):
	class Cow(Fact):
		pass

	class CowDisease(KnowledgeEngine):
		def __init__(self):
			KnowledgeEngine.__init__(self)

		@Rule(OR(Cow(disease='abortion'),Cow(disease='fever'),Cow(disease='weak body'),Cow(disease='weight loss')))
		def is_brucellosis(self,disease='Brucellosis'):
			self.disease = disease
			
		@Rule(OR(Cow(disease='abortion'),Cow(disease='nerve disorder'),Cow(disease='reproduction disorder'),Cow(disease='diarrhea'),Cow(disease='death')))
		def is_ibr(self,disease='Infection Bovine Rinotracheitis'):
			self.disease = disease
			
		@Rule(OR(Cow(disease='weight loss'),Cow(disease='diarrhea'),Cow(disease='trembling body'),Cow(disease='decreased milk production'),Cow(disease='death')))
		def is_johnes(self,disease="Johnes's Disease"):
			self.disease = disease
			
		@Rule(OR(Cow(disease='fever'),Cow(disease='bloody discharge'),Cow(disease='hard to breathe'),Cow(disease='death'),Cow(disease='darker eyes'),Cow(disease='depression'),Cow(disease='rapid breathing'),Cow(disease='increase pulse rate'),Cow(disease='stagger'),Cow(disease='seizure spasm'),Cow(disease='out of saliva')))
		def is_anthrax(self,disease='Anthrax'):
			self.disease = disease
			
		@Rule(OR(Cow(disease='fetal infection'),Cow(disease='decreased milk production'),Cow(disease='respiratory disorder'),Cow(disease='decreased appetite')))
		def is_madcow(self,disease='Mad Cow Disease'):
			self.disease = disease
			
			
		@Rule(OR(Cow(disease='diarrhea'),Cow(disease='death'),Cow(disease='decreased appetite'),Cow(disease='blood coming out of nose')))
		def is_bvd(self,disease='Bovine Viral Diarrhea'):
			self.disease = disease

		@Rule(OR(Cow(disease='difficult in walking'),Cow(disease='excess salivary secretion'),Cow(disease='wound lesion'),Cow(disease='fever')))
		def is_fmd(self,disease='Foot and Mouth Disease'):
			self.disease = disease
			
	

	if len(sympList) ==1:
		engine = CowDisease()
		engine.reset()
		engine.declare(Cow(disease=sympList[0]))
		# engine.run()
		# print(dir(engine))
		# print(engine.disease)
		return engine
	elif len(sympList) ==2:
		engine = CowDisease()
		engine.reset()
		engine.declare(Cow(disease=sympList[0]),Cow(disease=sympList[1]))
		return engine
	elif len(sympList) ==3:
		engine = CowDisease()
		engine.reset()
		engine.declare(Cow(disease=sympList[0]),Cow(disease=sympList[1]),Cow(disease=sympList[2]))
		return engine
	elif len(sympList) ==4:
		engine = CowDisease()
		engine.reset()
		engine.declare(Cow(disease=sympList[0]),Cow(disease=sympList[1]),Cow(disease=sympList[2]),Cow(disease=sympList[3]))
		return engine
	elif len(sympList) ==5:
		engine = CowDisease()
		engine.reset()
		engine.declare(Cow(disease=sympList[0]),Cow(disease=sympList[1]),Cow(disease=sympList[2]),Cow(disease=sympList[3]),Cow(disease=sympList[4]))
		return engine
	elif len(sympList) ==6:
		engine = CowDisease()
		engine.reset()
		engine.declare(Cow(disease=sympList[0]),Cow(disease=sympList[1]),Cow(disease=sympList[2]),Cow(disease=sympList[3]),Cow(disease=sympList[4]),Cow(disease=sympList[5]))
		return engine
	elif len(sympList) ==7:
		engine = CowDisease()
		engine.reset()
		engine.declare(Cow(disease=sympList[0]),Cow(disease=sympList[1]),Cow(disease=sympList[2]),Cow(disease=sympList[3]),Cow(disease=sympList[4]),Cow(disease=sympList[5]),Cow(disease=sympList[6]))
		return engine
	elif len(sympList) ==8:
		engine = CowDisease()
		engine.reset()
		engine.declare(Cow(disease=sympList[0]),Cow(disease=sympList[1]),Cow(disease=sympList[2]),Cow(disease=sympList[3]),Cow(disease=sympList[4]),Cow(disease=sympList[5]),Cow(disease=sympList[6]),Cow(disease=sympList[7]))
		return engine
	elif len(sympList) ==9:
		engine = CowDisease()
		engine.reset()
		engine.declare(Cow(disease=sympList[0]),Cow(disease=sympList[1]),Cow(disease=sympList[2]),Cow(disease=sympList[3]),Cow(disease=sympList[4]),Cow(disease=sympList[5]),Cow(disease=sympList[6]),Cow(disease=sympList[7]),Cow(disease=sympList[8]))
		return engine
	elif len(sympList) ==10:
		engine = CowDisease()
		engine.reset()
		engine.declare(Cow(disease=sympList[0]),Cow(disease=sympList[1]),Cow(disease=sympList[2]),Cow(disease=sympList[3]),Cow(disease=sympList[4]),Cow(disease=sympList[5]),Cow(disease=sympList[6]),Cow(disease=sympList[7]),Cow(disease=sympList[8]),Cow(disease=sympList[9]))
		return engine


# def ask_cow(request):
# 	if request.method == "POST":
# 		n = request.POST.getlist('symptom')
# 		print(n)
# 		print(len(n))
# 		l=cowexpert(n)
# 		l.run()
# 		print(dir(l))
# 		print(l.run())
# 		print(l.disease)
# 		list_of_symptoms = [i.symptom for i in CowSym.objects.all()]
# 		dis_info = CowDisInfo.objects.filter(disease = l.disease) 
# 		list_sym = [CowSym.objects.filter(symptom = i)[0] for i in dis_info[0].sym.split(',') if i in list_of_symptoms]
# 		print(list_sym)
# 		print(dis_info)
# 		prescription_info = Prescription.objects.filter(disease = l.disease) 
# 		if len(prescription_info)>0:
# 			prescription = prescription_info[0].prescription
# 		else:
# 			prescription = ''
# 		return render(request,"result.html",{'info':dis_info[0],'symptoms':list_sym,'prescription':prescription})


# 	return render(request,"cow_form.html",{})


def ask_cow(request):
	if request.method == "POST":
		n = request.POST.getlist('symptom')
		print(n)
		s= ["fever","weak body","weight loss","abortion","nerve disorder","reproduction disorder","diarrhea","death","trembling body","decreased milk production","hard to breathe","darker eyes","depression","rapid breathing","increase pulse rate","seizure spasm","stagger","out of saliva","fetal infection","respiratory disorder","decreased appetite","blood coming out of nose","excess salivary secretion","difficult in walking","wound lesion"]
		print(n)
		print('check: ',len(n)==len(s))
		res = dict(zip(s, n))
		print(res)
		
		message,dis,table = certainty("cow",res)
		if message == 'none':
			return render(request,"cow_form.html",{})
		else:
		
			list_of_symptoms = [i.symptom for i in CowSym.objects.all()]
			dis_info = CowDisInfo.objects.filter(disease = dis) 
			list_sym = [CowSym.objects.filter(symptom = i)[0] for i in dis_info[0].sym.split(',') if i in list_of_symptoms]
			print(list_sym)
			print(dis_info)
			prescription_info = Prescription.objects.filter(disease = dis) 
			if len(prescription_info)>0:
				prescription = prescription_info[0].prescription
			else:
				prescription = ''
			return render(request,"result.html",{'info':dis_info[0],'symptoms':list_sym,'prescription':prescription,"message":message,'table':table})


	return render(request,"cow_form.html",{})



#CAT
def catexpert(sympList):
	class Cat(Fact):
		pass

	class CatDisease(KnowledgeEngine):
		def __init__(self):
			KnowledgeEngine.__init__(self)

		@Rule(OR(Cat(disease='lumps'),Cat(disease='swelling'),Cat(disease='skin infection'),Cat(disease='weight loss'),Cat(disease='lethargy'),Cat(disease='diarrhea'),Cat(disease='loss of appetite')))
		def is_cancer(self,disease='Cancer'):
			self.disease = disease
			
		@Rule(OR(Cat(disease='change in appetite'),Cat(disease='weight loss'),Cat(disease='excessive thirst'),Cat(disease='increased urination'),Cat(disease='lethargy'),Cat(disease='dehydration')))
		def is_diabetes(self,disease='Diabetes'):
			self.disease = disease
			
		@Rule(OR(Cat(disease='enlarged lymph nodes'),Cat(disease='fever'),Cat(disease='Anemia'),Cat(disease='weight loss'),Cat(disease='poor appetite'),Cat(disease='diarrhea'),Cat(disease='dental disease'),Cat(disease='sneezing'),Cat(disease='discharge from eyes or nose')))
		def is_fiv(self,disease="Feline Immunodeficiency Virus (FIV)"):
			self.disease = disease
			
		@Rule(OR(Cat(disease='loss of appetite'),Cat(disease='weight loss'),Cat(disease='abcesses'),Cat(disease='fever'),Cat(disease='respiratory infections'),Cat(disease='seizure'),Cat(disease='jaundice'),Cat(disease='diarrhea'),Cat(disease='lethargy')))
		def is_felv(self,disease='Feline Leukemia Virus (FelV)'):
			self.disease = disease
			
		@Rule(OR(Cat(disease='cough'),Cat(disease='breathing difficulties'),Cat(disease='depression'),Cat(disease='loss of appetite'),Cat(disease='weight loss'),Cat(disease='vomiting'),Cat(disease='lethargy'),Cat(disease='death')))
		def is_heartworm(self,disease='Heartworm'):
			self.disease = disease	
			
		@Rule(OR(Cat(disease='changes in behavior'),Cat(disease='loss of appetite'),Cat(disease='weakness'),Cat(disease='paralysis'),Cat(disease='seizure'),Cat(disease='death')))
		def is_rabies(self,disease='Rabies'):
			self.disease = disease

		@Rule(OR(Cat(disease='skin lesions'),Cat(disease='bald patches')))
		def is_ringworm(self,disease='Ringworm'):
			self.disease = disease

		@Rule(OR(Cat(disease='sneezing'),Cat(disease='loss of appetite'),Cat(disease='runny nose'),Cat(disease='cough'),Cat(disease='gagging'),Cat(disease='fever'),Cat(disease='breathing difficulties'),Cat(disease='squinting')))
		def is_uri(self,disease='Upper Respiratory Infections'):
			self.disease = disease

		@Rule(OR(Cat(disease='diarrhea'),Cat(disease='weight loss'),Cat(disease='bloody stool'),Cat(disease='cough'),Cat(disease='worms visible in stool'),Cat(disease='vomiting'),Cat(disease='Anemia'),Cat(disease='constipation')))
		def is_worms(self,disease='Worms'):
			self.disease = disease

		@Rule(OR(Cat(disease='increased urination'),Cat(disease='bloody or cloudy urine'),Cat(disease='weight loss'),Cat(disease='vomiting'),Cat(disease='diarrhea'),Cat(disease='excessive thirst')))
		def is_kidneydisease(self,disease='Kidney Disease'):
			self.disease = disease

		@Rule(OR(Cat(disease='vomiting'),Cat(disease='loss of appetite'),Cat(disease='fever'),Cat(disease='abdominal pain'),Cat(disease='diarrhea')))
		def is_pancreatitis(self,disease='Pancreatitis'):
			self.disease = disease
			
		
			
		
			

	if len(sympList) ==1:
		engine = CatDisease()
		engine.reset()
		engine.declare(Cat(disease=sympList[0]))
		
		return engine
	elif len(sympList) ==2:
		engine = CatDisease()
		engine.reset()
		engine.declare(Cat(disease=sympList[0]),Cat(disease=sympList[1]))
		return engine
	elif len(sympList) ==3:
		engine = CatDisease()
		engine.reset()
		engine.declare(Cat(disease=sympList[0]),Cat(disease=sympList[1]),Cat(disease=sympList[2]))
		return engine
	elif len(sympList) ==4:
		engine = CatDisease()
		engine.reset()
		engine.declare(Cat(disease=sympList[0]),Cat(disease=sympList[1]),Cat(disease=sympList[2]),Cat(disease=sympList[3]))
		return engine
	elif len(sympList) ==5:
		engine = CatDisease()
		engine.reset()
		engine.declare(Cat(disease=sympList[0]),Cat(disease=sympList[1]),Cat(disease=sympList[2]),Cat(disease=sympList[3]),Cat(disease=sympList[4]))
		return engine
	elif len(sympList) ==6:
		engine = CatDisease()
		engine.reset()
		engine.declare(Cat(disease=sympList[0]),Cat(disease=sympList[1]),Cat(disease=sympList[2]),Cat(disease=sympList[3]),Cat(disease=sympList[4]),Cat(disease=sympList[5]))
		return engine
	elif len(sympList) ==7:
		engine = CatDisease()
		engine.reset()
		engine.declare(Cat(disease=sympList[0]),Cat(disease=sympList[1]),Cat(disease=sympList[2]),Cat(disease=sympList[3]),Cat(disease=sympList[4]),Cat(disease=sympList[5]),Cat(disease=sympList[6]))
		return engine
	elif len(sympList) ==8:
		engine = CatDisease()
		engine.reset()
		engine.declare(Cat(disease=sympList[0]),Cat(disease=sympList[1]),Cat(disease=sympList[2]),Cat(disease=sympList[3]),Cat(disease=sympList[4]),Cat(disease=sympList[5]),Cat(disease=sympList[6]),Cat(disease=sympList[7]))
		return engine
	elif len(sympList) ==9:
		engine = CatDisease()
		engine.reset()
		engine.declare(Cat(disease=sympList[0]),Cat(disease=sympList[1]),Cat(disease=sympList[2]),Cat(disease=sympList[3]),Cat(disease=sympList[4]),Cat(disease=sympList[5]),Cat(disease=sympList[6]),Cat(disease=sympList[7]),Cat(disease=sympList[8]))
		return engine
	elif len(sympList) ==10:
		engine = CatDisease()
		engine.reset()
		engine.declare(Cat(disease=sympList[0]),Cat(disease=sympList[1]),Cat(disease=sympList[2]),Cat(disease=sympList[3]),Cat(disease=sympList[4]),Cat(disease=sympList[5]),Cat(disease=sympList[6]),Cat(disease=sympList[7]),Cat(disease=sympList[8]),Cat(disease=sympList[9]))
		return engine


# def ask_cat(request):
# 	if request.method == "POST":
# 		n = request.POST.getlist('symptom')
# 		print(n)
# 		print(len(n))
# 		l=catexpert(n)
# 		l.run()
# 		print(dir(l))
# 		print(l.run())
# 		print(l.disease)
# 		list_of_symptoms = [i.symptom for i in CatSym.objects.all()]
# 		dis_info = CatDisInfo.objects.filter(disease = l.disease) 
# 		list_sym = [CatSym.objects.filter(symptom = i)[0] for i in dis_info[0].sym.split(',') if i in list_of_symptoms]
# 		print(list_sym)
# 		print(dis_info)
# 		prescription_info = Prescription.objects.filter(disease = l.disease) 
# 		if len(prescription_info)>0:
# 			prescription = prescription_info[0].prescription
# 		else:
# 			prescription = ''
# 		return render(request,"result.html",{'info':dis_info[0],'symptoms':list_sym,'prescription':prescription})


# 	return render(request,"cat_form.html",{})


def ask_cat(request):
	if request.method == "POST":
		n = request.POST.getlist('symptom')
		print(n)
		s = ["lumps","swelling","skin infection","weight loss","lethargy","diarrhea","loss of appetite","change in appetite","excessive thirst","increased urination","dehydration","enlarged lymph nodes","fever","cough","Anemia","dental disease","discharge from eyes or nose","sneezing","abcesses","respiratory infections","seizure","jaundice","breathing difficulties","depression","vomiting","death","paralysis","weakness","changes in behavior","skin lesions","bald patches","runny nose","gagging","squinting","bloody stool","worms visible in stool","constipation","bloody or cloudy urine","abdominal pain",'itchiness']		
		print(n)

		print(len(n)==len(s))
		res = dict(zip(s, n))
		print(res)
		res = dict(zip(s, n))
		print(res)
		
		message,dis,table = certainty("cat",res)
		if message == 'none':
			return render(request,"cat_form.html",{})
		else:
			list_of_symptoms = [i.symptom for i in CatSym.objects.all()]
			dis_info = CatDisInfo.objects.filter(disease = dis) 
			list_sym = [CatSym.objects.filter(symptom = i)[0] for i in dis_info[0].sym.split(',') if i in list_of_symptoms]
			print(list_sym)
			print(dis_info)
			prescription_info = Prescription.objects.filter(disease = dis) 
			if len(prescription_info)>0:
				prescription = prescription_info[0].prescription
			else:
				prescription = ''
			return render(request,"result.html",{'info':dis_info[0],'symptoms':list_sym,'prescription':prescription,'message':message,'table':table})


	return render(request,"cat_form.html",{})



#DOG
def dogexpert(sympList):
	class Dog(Fact):
		pass

	class DogDisease(KnowledgeEngine):
		def __init__(self):
			KnowledgeEngine.__init__(self)

		@Rule(OR(Dog(disease='lumps'),Dog(disease='swelling'),Dog(disease='skin infection'),Dog(disease='weight loss'),Dog(disease='lethargy'),Dog(disease='diarrhea'),Dog(disease='loss of appetite')))
		def is_cancer(self,disease='Cancer'):
			self.disease = disease
			
		@Rule(OR(Dog(disease='change in appetite'),Dog(disease='weight loss'),Dog(disease='excessive thirst'),Dog(disease='increased urination'),Dog(disease='lethargy'),Dog(disease='dehydration')))
		def is_diabetes(self,disease='Diabetes'):
			self.disease = disease
			
		@Rule(OR(Dog(disease='gagging'),Dog(disease='fever'),Dog(disease='cough'),Dog(disease='nasal discharge')))
		def is_kennelcough(self,disease="Kennel Cough"):
			self.disease = disease
			
		@Rule(OR(Dog(disease='loss of appetite'),Dog(disease='lethargy'),Dog(disease='vomiting'),Dog(disease='bloody diarrhea')))
		def is_parvovirus(self,disease='Parvovirus'):
			self.disease = disease
			
		@Rule(OR(Dog(disease='cough'),Dog(disease='breathing difficulties'),Dog(disease='depression'),Dog(disease='loss of appetite'),Dog(disease='weight loss'),Dog(disease='vomiting'),Dog(disease='lethargy')))
		def is_heartworm(self,disease='Heartworm'):
			self.disease = disease	
			
		@Rule(OR(Dog(disease='changes in behavior'),Dog(disease='loss of appetite'),Dog(disease='weakness'),Dog(disease='paralysis'),Dog(disease='seizure'),Dog(disease='death')))
		def is_rabies(self,disease='Rabies'):
			self.disease = disease

		@Rule(OR(Dog(disease='skin lesions'),Dog(disease='bald patches')))
		def is_ringworm(self,disease='Ringworm'):
			self.disease = disease

		@Rule(OR(Dog(disease='itchiness'),Dog(disease='pain'),Dog(disease='odor'),Dog(disease='scabs'),Dog(disease='swelling or redness in the ear canal')))
		def is_earinfection(self,disease='Ear Infection'):
			self.disease = disease	
		
			
	if len(sympList) ==1:
		engine = DogDisease()
		engine.reset()
		engine.declare(Dog(disease=sympList[0]))
		
		return engine
	elif len(sympList) ==2:
		engine = DogDisease()
		engine.reset()
		engine.declare(Dog(disease=sympList[0]),Dog(disease=sympList[1]))
		return engine
	elif len(sympList) ==3:
		engine = DogDisease()
		engine.reset()
		engine.declare(Dog(disease=sympList[0]),Dog(disease=sympList[1]),Dog(disease=sympList[2]))
		return engine
	elif len(sympList) ==4:
		engine = DogDisease()
		engine.reset()
		engine.declare(Dog(disease=sympList[0]),Dog(disease=sympList[1]),Dog(disease=sympList[2]),Dog(disease=sympList[3]))
		return engine
	elif len(sympList) ==5:
		engine = DogDisease()
		engine.reset()
		engine.declare(Dog(disease=sympList[0]),Dog(disease=sympList[1]),Dog(disease=sympList[2]),Dog(disease=sympList[3]),Dog(disease=sympList[4]))
		return engine
	elif len(sympList) ==6:
		engine = DogDisease()
		engine.reset()
		engine.declare(Dog(disease=sympList[0]),Dog(disease=sympList[1]),Dog(disease=sympList[2]),Dog(disease=sympList[3]),Dog(disease=sympList[4]),Dog(disease=sympList[5]))
		return engine
	elif len(sympList) ==7:
		engine = DogDisease()
		engine.reset()
		engine.declare(Dog(disease=sympList[0]),Dog(disease=sympList[1]),Dog(disease=sympList[2]),Dog(disease=sympList[3]),Dog(disease=sympList[4]),Dog(disease=sympList[5]),Dog(disease=sympList[6]))
		return engine
	elif len(sympList) ==8:
		engine = DogDisease()
		engine.reset()
		engine.declare(Dog(disease=sympList[0]),Dog(disease=sympList[1]),Dog(disease=sympList[2]),Dog(disease=sympList[3]),Dog(disease=sympList[4]),Dog(disease=sympList[5]),Dog(disease=sympList[6]),Dog(disease=sympList[7]))
		return engine
	elif len(sympList) ==9:
		engine = DogDisease()
		engine.reset()
		engine.declare(Dog(disease=sympList[0]),Dog(disease=sympList[1]),Dog(disease=sympList[2]),Dog(disease=sympList[3]),Dog(disease=sympList[4]),Dog(disease=sympList[5]),Dog(disease=sympList[6]),Dog(disease=sympList[7]),Dog(disease=sympList[8]))
		return engine
	elif len(sympList) ==10:
		engine = DogDisease()
		engine.reset()
		engine.declare(Dog(disease=sympList[0]),Dog(disease=sympList[1]),Dog(disease=sympList[2]),Dog(disease=sympList[3]),Dog(disease=sympList[4]),Dog(disease=sympList[5]),Dog(disease=sympList[6]),Dog(disease=sympList[7]),Dog(disease=sympList[8]),Dog(disease=sympList[9]))
		return engine


# def ask_dog(request):
# 	if request.method == "POST":
# 		n = request.POST.getlist('symptom')
# 		print(n)
# 		print(len(n))
# 		l=dogexpert(n)
# 		l.run()
# 		print(dir(l))
# 		print(l.run())
# 		print(l.disease)

# 		list_of_symptoms = [i.symptom for i in DogSym.objects.all()]
# 		print(list_of_symptoms)
# 		dis_info = DogDisInfo.objects.filter(disease = l.disease) 
# 		print(dis_info)
# 		list_sym = [DogSym.objects.filter(symptom = i)[0] for i in dis_info[0].sym.split(',') if i in list_of_symptoms]
# 		print(list_sym)
# 		print(dis_info)
# 		prescription_info = Prescription.objects.filter(disease = l.disease) 
# 		if len(prescription_info)>0:
# 			prescription = prescription_info[0].prescription
# 		else:
# 			prescription = ''
# 		return render(request,"result.html",{'info':dis_info[0],'symptoms':list_sym,'prescription':prescription})


# 	return render(request,"dog_form.html",{})

def ask_dog(request):
	if request.method == "POST":
		n = request.POST.getlist('symptom')
		s = ["lumps","swelling","skin infection","weight loss","lethargy","diarrhea","loss of appetite","change in appetite","excessive thirst","increased urination","dehydration","gagging","cough","fever","nasal discharge","vomiting","bloody diarrhea","breathing difficulties","depression","changes in behavior","weakness","paralysis","seizure","death","skin lesions","bald patches","itchiness","pain","odor","scabs","swelling or redness in the ear canal"]
		print(n)

		print(len(n)==len(s))
		res = dict(zip(s, n))
		print(res)
		
		message,dis,table = certainty("dog",res)
		if message == 'none':
			return render(request,"dog_form.html",{})
		else:
			list_of_symptoms = [i.symptom for i in DogSym.objects.all()]
			print(list_of_symptoms)
			dis_info = DogDisInfo.objects.filter(disease = dis) 
			print(dis_info)
			list_sym = [DogSym.objects.filter(symptom = i)[0] for i in dis_info[0].sym.split(',') if i in list_of_symptoms]
			print(list_sym)
			print(dis_info)
			prescription_info = Prescription.objects.filter(disease = dis) 
			if len(prescription_info)>0:
				prescription = prescription_info[0].prescription
			else:
				prescription = ''
			return render(request,"result.html",{'info':dis_info[0],'symptoms':list_sym,'prescription':prescription,'message':message,'table':table})


	return render(request,"dog_form.html",{})




def info(request,id):
	dis_info = AnimalInfo.objects.filter(info_id = id)[0] 
	print(dis_info.imagelink)
	split = dis_info.imagelink.split(',')
	a_name = []
	a_image = []
	for i in range(0,len(split),2):
		a_name.append(split[i])
		a_image.append(split[i+1])
	print(a_name,' ',a_image)

	

	return render(request,"info.html",{'info':dis_info,'a_name':a_name,'a_image':a_image})