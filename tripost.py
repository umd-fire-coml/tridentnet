import json
import os 

def processRoiJson(self, batch_size, jsonDir, consider_misc_categories){
    data = json.load(jsonDir)
    
    image_set = []
    for annotation in data:
    
        if(consider_misc_categories and (annotation['category_id'] == 8 or annotation['category_id'] == 9)): 
            #add this annotation
            bbox = annotation['bbox']
            cat_id = annotation['category_id']
            im_id = annotation['image_id']
            sc = annotation['score']
    
            image = plt.imread()
            
    
        elif(not consider_misc_categories and (annotation['category_id'] == 8 or annotation['category_id'] == 9)):
            #do not consider these annotations
            
        else:
            bbox= annotation['bbox']
            cat_id = annotation['category_id']
            im_id = annotation['image_id']
            sc = annotation['score']
    
}