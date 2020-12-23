#python 02_Dlib_test.py
#Criar arquivo xml com as imagens de teste
import dlib

print(dlib.test_simple_object_detector('mask.xml', "mask.svm"))
