def get_counts(scores, classes, thresh = 0.80):
    ## Get predictions that are above threshold
    pred_probs = scores[scores >= thresh]
    pred_labels = classes[scores >= thresh]
    df = pd.DataFrame({'scores': pred_probs, 'class_id': pred_labels})
    
    ## Mapping of class IDs to labels
    df['label'] = df.class_id.map(label_mapping)
    
    ## Value counts
    vc = df.label.value_counts()
    out = dict()
    
    for lab in list_classes:
        try:
            out[lab] = vc[lab]
        except:
            out[lab] = 0
    return out





def annotate_with_metrics(frame, scores, classes, thresh = 0.80, show_plot=False):
    
    ## Get counts
    counts = get_counts(scores, classes, thresh = 0.80)
    #print(counts)
    
    cv2_im_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    source_img = Image.fromarray(cv2_im_rgb)

    width_image = source_img.size[0]
    height_image = source_img.size[1]
    width_box = 600
    height_box = 300
    font_size = 75
    box_color = (132,139,139)
    text_color = (255,255,255)
    #font = ImageFont.truetype("../../../../config/fonts/arial.ttf", font_size)
    font = ImageFont.truetype("fonts/arial.ttf", font_size)

    draw = ImageDraw.Draw(source_img)
    draw.rectangle(((0, 00), (width_box, height_box)), fill=box_color)
    #draw.text((20, 70), "something123")
    draw.text((int(0.05*width_box), int(0.05*height_image)),'chefs:',text_color,font=font)
    draw.text((int(0.05*width_box), int(0.10*height_image)),'in progress:',text_color,font=font)
    draw.text((int(0.05*width_box), int(0.15*height_image)),'in oven:',text_color,font=font)
    draw.text((int(0.89*width_box), int(0.05*height_image)), str(counts['chef']),text_color,font=font)
    draw.text((int(0.89*width_box), int(0.10*height_image)), str(counts['pizza in progress']),text_color,font=font)
    draw.text((int(0.89*width_box), int(0.15*height_image)), str(counts['pizza in oven']),text_color,font=font)
    
    if show_plot is True:
        plt.figure(figsize=IMAGE_SIZE)
        plt.imshow(source_img)
        
    source_img = np.array(source_img)[:,:,::-1]
    
    return source_img, counts  
