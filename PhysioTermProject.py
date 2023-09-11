# To-Do:
# Tentative Problem: You might need to make a sort of reset thing for the title and the body labels because if you change
# anything about them in any of the functions that set up various windows, it might be annoying to fix that
# Keep chugging away at brain and whatever other sections.
# Maybe make a systematic sorta thing for buttons in the mb (main box)... it could a 2d arrays with buttons and their coordinates
# and a function that places each button individually but that is complicated
# Buttons: try to see how cool you can make them, you will have to figure out how to place them, if you want an arrow
# Pointing to the structure frm the button. The buttons should hopefully be transparent or not look really basic. You can
# add color, idk whatelse.
# resize brain picture (systematic way to resize images? and move them based on their dimensions? photoshopping pics to get rid of text- if needed)
# move buttons on brain screen on to the brain
# help button?
# photoshop?
#make a debugger window for resizing stuff

import tkinter as tk
from tkinter import Tk
from tkinter import Canvas
from tkinter import Button
from tkinter import Label
from tkinter import Frame
from tkinter import *
from PIL import ImageTk, Image
from itertools import count, cycle
import time
import os
################################################## GIF #################################################################
class ImageLabel(tk.Label):
    """
    A Label that displays images, and plays them if they are gifs
    :im: A PIL Image instance or a string filename
    """

    # def __init__(self):
    #    self.frames = None

    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        frames = []
        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)
        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)
########################################################################################################################
######### Help Window #################################################################################################

about = "\nHow to use this program:\n\n" \
         "Click through the buttons of the side bar or the main screen to learn more about the brain"\
         ", the neuron, or the neuropsychology of various psychopathologies. If you want to go back "\
         "to the previous screen, click the \"Back\" button on the bottom right of the screen. To go "\
         "back to the home screen, click the \"Home\" button.\n\n"\
         "Why I made this program: \n\n"\
         "During high school and my freshman year of college, I took many classes in computer science, "\
         "but after changing my major from physics to psychology, I haven't had as many opportunities "\
         "to incorporate my those skills into my class work. Additionally, I have always been "\
         "interested in learning more about the brain, and its important parts. So, as soon as this project"\
         " was introduced, I knew exactly what I wanted to do. When I started working on this project, I wanted to include so much information " \
        "that it would have ended up being too much work. For example, I wanted to go into the functions of different neurotransmitters, the neuropsychology behind treatments for psychopathology, the inner-workings " \
        "of the action potential, and additional descriptions of other parts of the brain. I also wanted to add a fill-in-the-blanks quiz so that students could study the parts of the brain." \
        "\n\nThis project has been very "\
         "rewarding for me as I have been able to practice my programming skills using Python and Tkinter to create this interactive display. I have also learned a lot more about the brain " \
        "and the current research on structures of the brain, and neuropsychopathology. Also, this program could also be rewarding for others as it can be " \
        "used to study parts of the brain. I included diagrams of the brain from the Kalat Biological Psychology textbook which students in Physiological Psychology should be familiar with. " \
        "Lastly, this could also be rewarding to individuals who are just interested in psychology, want to learn more about the brain, and the research behind abnormal neuropsychological functioning."

references = "References:\n\n" \
             "There are many references used through out this program. They are used cited using a superscripted numbers" \
             " such as \'¹\'. Below are the references with their associated superscript\n\n" \
             "¹American Psychiatric Association. (2022). Diagnostic and statistical manual of mental disorders (5th ed., text rev.). https://doi.org/10.1176/appi.books.9780890425787"+"\n\n" \
             "²Cole, E. J. et al., (2020). Stanford accelerated intelligent neuromodulation therapy for treatment-resistant depression. The American Journal of Psychiatry, 177(8), 716–726. https://doi-org.ezproxy.bethel.edu/10.1176/appi.ajp.2019.19070720"+"\n\n" \
             "³Sylvester CM, Corbetta M, Raichle ME, Rodebaugh TL, Schlaggar BL, Sheline YI, Zorumski CF, Lenze EJ (2012): Functional network dysfunction in anxiety and anxiety disorders. Trends Neurosci 35: 527– 535."+"\n\n" \
             "⁴Barkley, R. A. (1997). Behavioral inhibition, sustained attention, and executive functions: Constructing a unifying theory of ADHD. Psychological Bulletin, 121(1), 65–94. https://doi-org.ezproxy.bethel.edu/10.1037/0033-2909.121.1.65"+"\n\n" \
             "⁵Baxter, M. G., &; Croxson, P. L. (2012). Facing the role of the amygdala in emotional information processing. Proceedings of the National Academy of Sciences, 109(52), 21180–21181. https://doi.org/10.1073/pnas.1219167110 "+"\n\n" \
             "⁶Kozlovskiy, S. A., Nikonova, E. Y., Pyasik, M. M., & Velichkovsky, B. M. (2012). The cingulate cortex and human memory processes. Psychology in Russia, 5, 231."+"\n\n" \
             "⁷Rudebeck, P. H., Putnam, P. T., Daniels, T. E., Yang, T., Mitz, A. R., Rhodes, S. E., & Murray, E. A. (2014). A role for primate subgenual cingulate cortex in sustaining autonomic arousal. Proceedings of the National Academy of Sciences, 111(14), 5391–5396. https://doi.org/10.1073/pnas.1317695111 "+"\n\n" \
             "⁸RajMohan, V., &amp; Mohandas, E. (2007). The limbic system. Indian Journal of Psychiatry, 49(2), 132. https://doi.org/10.4103/0019-5545.33264 "+"\n\n" \
             "⁹Isa, T., Marquez-Legorreta, E., Grillner, S., & Scott, E. K. (2021). The tectum/superior colliculus as the vertebrate solution for spatial sensory integration and action. Current Biology, 31(11). https://doi.org/10.1016/j.cub.2021.04.001"+"\n\n" \
             "¹⁰Camchong, J., MacDonald III, A. W., Bell, C., Mueller, B. A., & Lim, K. O. (2011). Altered functional and anatomical connectivity in schizophrenia. Schizophrenia bulletin, 37(3), 640-650.\n\n" \
             "¹¹Aouizerate, B., Guehl, D., Cuny, E., Rougier, A., Bioulac, B., Tignol, J., & Burbaud, P. (2004). Pathophysiology of obsessive–compulsive disorder: a necessary link between phenomenology, neuropsychology, imagery and physiology. Progress in neurobiology, 72(3), 195-221.\n\n" \
             "¹²Etkin, A., Egner, T., & Kalisch, R. (2011). Emotional processing in anterior cingulate and medial prefrontal cortex. Trends in cognitive sciences, 15(2), 85-93."

global about_state
about_state = 0

def help():
    win = Tk()
    win.title("Help")

    global body_about, switch_b
    switch_b = Button(win, text="References", bg="Black", fg="White", height=2, width=15, font=('Lucida Sans', 13), command=switch)
    switch_b.grid(row=0, column=0)
    bod = Frame(win, width=600, height=600)
    bod.grid(row=1, column=0)
    body_about = Label(bod, wraplength=500, justify="left", font=('Lucida Sans', 13), text=about)
    body_about.pack()
    win.mainloop()

def switch():
    global about_state, switch_b
    if about_state == 0:
        body_about.configure(text=references, font=('Lucida Sans', 10))
        switch_b.configure(text="About")
        about_state = 1
    else:
        body_about.configure(text=about, font=('Lucida Sans', 13))
        switch_b.configure(text="References")
        about_state = 0

############################# FUNCTIONS ###########################################################

def center_image(label, img): # returns the padding to center a picture in mb (returns padx, pady)
    #print(label, img)
    #print("padx=", str((1434-img.width())/2), "pady="+str((1080-img.height())/2))
    label.pack(padx=(1434-img.width())/2, pady=(1080-img.height())/2)

def destroy(f):
    for i in range(len(f)):
        f[i].destroy()

def hide(f):
    for i in range(len(f)):
        f[i].place(x=2000, y=0)

def show(f, x, y): # the same thing as move
    f.place(x=x, y=y)

def restart():
    #print(current)
    global history
    history.pop(0)(0)
    history = []
    home(1)  # activates the home screen
    # show(sb, 0, 0)

def back():
    global history
    #Fprint("Current: "+str(current)+" , Previous: "+str(prev))
    history.pop(0)(0)
    history.pop(0)(1)

def set_location(c, p): #for back button
    global current, prev
    current = c
    prev = p

def home(state):
    if state == 1:
        history.insert(0, home)
        hide([mb])
        show(gif, x=(xd / 4) + 145, y=(yd / 3) - 150)
        body.configure(text="Please choose which area of neuropsychology you would like to learn about")
        title.configure(text="Home")
        psycho_b.pack(side=BOTTOM, pady=30)
        neuron_b.pack(side=BOTTOM, pady=30)
        brain_b.pack(side=BOTTOM, pady=30)
    else:
        hide([brain_b, neuron_b, psycho_b, gif])
        show(mb, (xd / 4) + 51, 0)

def neuron(state):
    if state == 1:
        global history
        history.insert(0, neuron)

        title.configure(text="The Neuron")
        body.configure(
            text="The Neuron is the primary communicative cell that makes up the central and peripheral nervous system.\n"
                 "It is made of 4 main parts: The cell body, or soma, the dendrites, the axon, and the synapse.\n\n"
                 "Click on each button corresponding with the part of the neuron to learn more!")

        center_image(neuron_pic, neuron_p)

        xd = 600 #x_displacement
        axon_b.place(x=1350-xd, y=650)
        soma_b.place(x=675-xd, y=775)
        dendrites_b.place(x=700-xd, y=226)
        synapse_b.place(x=1630-xd, y=200)

    else:
        hide([axon_b, soma_b, dendrites_b, synapse_b, neuron_pic])

def brain(state):  # 1 = on, 0 = off, changes text, adds buttons on side bar (sb) and changes the main picture
    if state == 1:
        history.insert(0, brain)

        title.configure(text="The Brain")
        body.configure(text="The brain is the most complex and important part of the body. "
                            "It drives all of the necessary involuntary processes of the body, such as the beating of the heart, "
                            "breathing, and temperature regulation. It also controls all of our voluntary actions, sense perception, and "
                            "cognitive functions.\n\nThe brain can be split up into three sections, the hindbrain, the midbrain, and the forebrain (which includes the cerebral cortex and the limbic system)."
                            "\n\nClick on each section below to learn more.\n\n")

        forebrain_b.place(x=591, y=214)#side=BOTTOM, pady=30)
        hind_and_midbrain_b.place(x=300, y=748)
        limbic_b.place(x=590, y=400)

        center_image(lobes_pic, sections_of_the_brain)
    else:
        hide([forebrain_b, hind_and_midbrain_b, lobes_pic, limbic_b])

def forebrain(state):
    if state == 1:
        history.insert(0, forebrain)

        title.configure(text="The Cerebral Cortex")
        body.configure(text="The forebrain the is largest and phylogenetically newest section of the brain.\n\n"
                            "It is made up for four cortices, the frontal cortex, the parietal cortex, the temporal cortex, and the occipital cortex.\n\n"
                            "These structures are important for cognition, sensation, perception, and movement.")

        s = 50
        parietal_b.place(x=1432-512-s, y=238)
        frontal_b.place(x=131-s, y=238)
        occipital_b.place(x=1120-s, y=583)
        temporal_b.place(x=679-s, y=736)

        forebrain_pic.pack(padx=117-50, pady=111.5)

    else:
        hide([parietal_b, frontal_b, occipital_b, temporal_b, forebrain_pic])
        # PIC.configure(image='')
        # PIC.image = None

def hind_and_midbrain(state):
    if state == 1:
        history.insert(0, hind_and_midbrain)

        title.configure(text="The Hindbrain and The Midbrain", font=("Lucida Sans", 20))
        body.configure(text="The hindbrain and midbrain are the oldest structures of the brain and are responsible for many of the transportation and processing of sensory information and our body's involuntary processes.") #The Hindbrain, or the rhombencephalon, is in the bottom most part of the brain and connects to the spinal cord via the medulla

        medulla_b.place(x=667, y=833)
        pons_b.place(x=657, y=524)
        cerebellum_b.place(x=1116, y=491)
        spinalc_b.place(x=883, y=667)

        tectum_b.place(x=66, y=612)
        colliculus_b.place(x=78, y=535)
        tegmentum_b.place(x=181, y=706)

        center_image(hindbrain_pic, hindbrain_p)
    else:
        title.configure(font=("Lucida Sans", 30))
        hide([medulla_b, pons_b, cerebellum_b, spinalc_b, tectum_b, colliculus_b, tegmentum_b, nigra_b, hindbrain_pic])

def limbic(state):
    if state == 1:
        history.insert(0, limbic)

        title.configure(text="The Limbic System")
        body.configure(text="The limbic system, which consists of many components, is an essential part in the processing and expression of emotion⁸.")

        cingulate_b.place(x=183, y=182)
        thalamus_b.place(x=141, y=311)
        hypothalamus_b.place(x=156, y=433)
        hippocampus_b.place(x=150, y=646)
        amygdala_b.place(x=69, y=764)

        center_image(limbic_pic, limbic_p)
    else:
        hide([cingulate_b, thalamus_b, hypothalamus_b, hippocampus_b, amygdala_b, limbic_pic])

############# PSYCHOPATHOLOGY Fuctions ################################################################################

def psycho(state):
    if state == 1:
        history.insert(0, psycho)

        title.configure(text="Psychopathology")
        body.configure(text='Please choose which area of psychopathology you would like to learn about')
        title_path.configure(wraplength= 1920-600, text="Please note: The symptoms described are not a complete nor sufficient list. The full extent of criteria include much more detail that is dependent on the age and/or mental/physical state of the individual.")
        mb_psycho(1)
        hide([sym_t_path, neuro_t_path])
        depression_b.pack(pady=17)
        anxiety_b.pack(pady=17)
        adhd_b.pack(pady=17)
        schizo_b.pack(pady=17)
        ocd_b.pack(pady=17)
    else:
        hide([depression_b, anxiety_b, adhd_b, schizo_b, ocd_b])
        mb_psycho(0)

def mb_psycho(state):
    if state == 1:
        title_path.place(y=30, x=30)#((1920-530)/2)-(title_path.winfo_width()/2))
        sym_t_path.place(y=100, x=30)
        neuro_t_path.place(y=100, x=30+((1920-530)/2))
        neuro_path.place(y=100+50, x=30+((1920-530)/2))
        sym_path.place(y=100+50, x=30)
    else:
        hide([title_path, sym_t_path, neuro_t_path, neuro_path, sym_path])


def depression(state):
    if state == 1:
        title_path.configure(text="Major Depressive Disorder")
        sym_path.configure(text="According to the DSM-5¹, the basic criteria for a clinical diagnosis of adult Major Depressive Disorder include:\n\n"
                                "1. Depressed mood almost everyday for most of the day.\n\n"
                                "2. Noticeably diminished interest or pleasure in most activities.\n\n"
                                "3. Significant weight loss when not dieting, weight gain, or decrease/increase in appetite.\n\n"
                                "4. Insomnia or hypersomnia.\n\n"
                                "5. Psychomotor agitation or retardation.\n\n"
                                "6. Fatigue or loss of energy nearly every day.\n\n"
                                "7. Extreme feelings of worthlessness or excessive/inappropriate guilt.\n\n"
                                "8. Diminished ability to think, concentrate, or being indecisive.\n\n"
                                "9. Recurrent thoughts of death, suicidal ideation with or without a specific plan.")
        neuro_path.configure(text="     While the neuropsychology of the depression is quite complex, some interesting findings can be deduced from the work of Stanford University's Intelligent Neuromodulation Therapy "
                                  "for Treatment-Resistant Depression² Their intermittent theta-burst stimulation is a highly effective form of treatment for treatment-resistant depression (i.e., depression that is unable to "
                                  "be treated through medication or psychotherapy). Their treatment passes an eletrical current through a magnetic coil placed on top of the scalp and producing a high-intensity magnetic field that passes through the scalp, skull, and mininges to excite neuoronal tissue. "
                                  "The excite the left dorsolateral prefrontal cortex, which is hypothesized to indirectly inhibit the subgenual anterior cingulate cortex.\n\n"
                                  "     The left dorsolateral prefrontal cotex is responsible for higher cognitive functioning, such as changing the direction of attention, storing working memory, maintaining abstracted rules, and inhibition of inappropriate responses.\n"
                                  "The subgenual anterior singulate cortex is important for the regulation of emotional. Degeneration in the area is associated with depression and anhedonia⁷.\n\n"
                                  "     The implications of these results suggest that depression could be associated with less activity the in both the left dorsolateral prefrontal cortex and the subgenual anterior singulate cortex.")
        mb_psycho(1)

    else:
        mb_psycho(0)

def adhd(state):
    if state == 1:
        title_path.configure(text="Attention-Deficit/Hyperactivity Disorder (ADHD)")
        sym_path.configure(text="According to the DSM-5¹, the basic criteria for a clinical diagnosis of adult Attention-Deficit/Hyperactivity Disorder include:\n\n"
                                "1. A persistent pattern of inattention and/or hyperactivity-impulsivity that interferes with functioning of development.\n\n"
                                "   a. Inattention can include failure to give close attention to details, making careless mistakes at school, work, or other activities, and difficulty sustaining attention.\n\n"
                                "   b. Hyperactivity and impulsivity can include fidgeting, leaving seat in situations when remainig seated in expected, and running or climbing in inappropriate situations.\n\n"
                                "2. Presence of symptoms prior to age 12.\n\n"
                                "3. Symptoms are presented in two or more settings (e.g., at home, school, work, with friends, in other activities.\n\n"
                                "4. Symptoms interfere with, or reduce the quality of social, academic, or occupation functioning.\n\n"
                                "5. Symptoms do not occur exclusively during the course of other psychotic disorders, and are not better explained by a different disorder.")
        neuro_path.configure(text="     Research by Dr. Russell Barkley shows that the idea that ADHD is when a person fails to inhibit their fidgeting or distracting thoughts is a misconception."
                                  " Instead, ADHD should be a viewed as a failure of executing functioning. In his work, Dr. Barkley describes 3 networks that are responsible for executive functioning⁴.\n\n"
                                  "The three are:\n\n"
                                  "     1. The Frontal-Striatal Circuit: This circuit exists between the dorsolateral prefrontal cortex (DLPFC) and the basal ganglia. ADHD that impairs this circuit is associated with deficits in response suppression, freedom from distraction, working memory, and organization and planning.\n\n"
                                  "     2. The Frontal-Cerebellum Circuit: This circuit exists between the DLPFC, the basal ganglia, and the cerebellum. ADHD that impairs this circuit is associated with deficits in motor coordination, and problems with timing and timelines of behaviors.\n\n" 
                                  "     3. The Frontal-Limbic Circuit: This circuit exists between the frontal cortex, and the amygdala. ADHD that impairs this circuit is associated with deficits in emotional discontrol, motivation deficits, hyperactivity, impulsivity, and proneness to aggression.\n\n"
                                  "     Based on this information, there are many differing parts of the brain that are associated with ADHD, but the main ones are the DLPFC as it is important in executive functioning.")
        mb_psycho(1)
    else:
        mb_psycho(0)

def anxiety(state):
    if state == 1:
        title_path.configure(text="Generalized Anxiety Disorder")
        sym_path.configure(text="According to the DSM-5¹, the basic criteria for a clinical diagnosis of adult Generalized Anxiety Disorder include:\n\n"
                                "1. Excessive anxiety and worry occurring more days that not\n\n"
                                "2. The individual finds it difficult to control the worry\n\n"
                                "3. The anxiety and worry are associated with three (or more) of the following six symptoms\n\n"
                                "   a. Restlessness or feeling keyed up or on edge.\n\n"
                                "   b. Being easily fatigued\n\n"
                                "   c. Difficulty concentrating or mind going blank\n\n"
                                "   d. Irritability\n\n"
                                "   e. Muscle tension\n\n"
                                "   f. Sleep disturbance\n\n"
                                "4. The anxiety, worry, or physical symptoms cause significant distress or impairment in social occupation, or other important areas of functioning\n\n"
                                "5. The disturbance is not attributable to the physiological effects of a substance or another medical condition\n\n"
                                "6. The disturbance is not better explained by another mental disorder.")
        neuro_path.configure(text="     The general consensus with Generalized Anxiety Disorder is that is caused by an increased activity in the amygdala. "
                                  "But there is also research that looks at the association between different attention networks of the brain and anxiety. "
                                  "Work by Sylvester, et. al in 2012³ discovered that increased activity of the cingulo-opercular and ventral attention networks, along with decreased functioning of the fronto-parietal and default mode networks in associated with anxiety disorders. "
                                  "\n\n     The cingulo-opercular network is made up of portions of the dorsal anterior cingulate cortex and insula, and is important in detecting the need for changes in cognitive control.\n\n"
                                  "     The fronto-parietal network includes parts of the dorsolateral perfrontal cotex (PFC) and inferior parietal cortex. It is possible responsible for cognitive control.\n"
                                  "The ventral attention network includes parts of the ventrolateral PFC and temporal-parietal junction and is involved in switching one's attention to newly appearing stimuli.\n"
                                  "Lastly, the default mode network, which includes portions of the subgenual anterior singulate cortex, medial temporal lobe, and precuneus, is hypothesized to regulate emotion, plan for the future, and inspect-oneself.\n\n"
                                  "     Based on these findings, the neuropsychology of anxiety is associated with many disparate parts of the brain and not only the amygdala.")
        mb_psycho(1)

    else:
        mb_psycho(0)

def schizophrenia(state):
    if state == 1:
        title_path.configure(text="Schizophrenia")
        sym_path.configure(text="According to the DSM-5¹, the basic criteria for a clinical diagnosis of adult schizophrenia include:\n\n"
                                "1. Two+ of the following symptoms\n\n"
                                "   a. Delusions\n\n"
                                "   b. Hallucinations\n\n"
                                "   c. Disorganized Speech\n\n"
                                "   d. Grossly disorganized or catatonic behavior\n\n"
                                "   e. Negative symptoms\n\n"
                                "2. Deteriorated level of occupational, relational, or self-care functioning.\n\n"
                                "3. At least 6 months of continuous disturbance\n\n"
                                "4. No comorbidity with schizoaffective disorder, or depressive or bipolar disorder with psychotic features.\n\n"
                                "5. Symptoms are not due to the physiological effects of a substance\n\n")
        neuro_path.configure(text="     A study by Camchong, et al. in 2011¹⁰ showed that \"altered functional and anatomical connectivity in medial frontal and anterior cingulate gyri\" existed in the brains of schizophrenia patients. "
                                  "In addition, \"frontal connectivity in schizophrenia patients was positively associated with symptoms as well as with general cognitive ability measures.\"\n\n"
                                  "     The medial frontal and anterior cingulate gyri are responsible for the appraisal and expression of negative emotion, and even generating emotional responses¹²\n\n"
                                  "     Overall, based on the symptoms of schizophrenia, there is probably a widespread effect on the brain.")
        mb_psycho(1)

    else:
        mb_psycho(0)

def ocd(state):
    if state == 1:
        title_path.configure(text="Obsessive-Compulsive Disorder (OCD)")
        sym_path.configure(text="According to the DSM-5¹, the basic criteria for a clinical diagnosis of adult Obsessive-Compulsive Disorder include:\n\n"
                                "1. Presence of obsessions, compulsions, or both:\n\n"
                                "   Obsessions: recurrent, persistant, intrusive and unwated thoughts, urges, or images that in most  individuals bring anxiety or distress."
                                " Obsessions also include attempts by the individual to ignore or suppress such stimuli with some thought or action (i.e., by performing a compulsion).\n\n"
                                "   Compulsions: Repetitive behaviors that the individual feels driven to perform in response to an obsession or according to rules that must be applied rigidly. "
                                "The behaviors or mental acts are aimed at preventing or reducing anxiety or distress, or preventing a dreaded situation.\n\n"
                                "2. Obsessions or compulsions are time-consuming or cause clinically significant distress or impairment in social, occupational or other important areas of functions.\n\n"                                
                                "3. The obssessive-compulsive symptoms are not attributable to the physiological effects of a substance.\n\n"
                        
                                "4. The disturbance is not better explained by the symptoms of another mental disorder.\n\n")
        neuro_path.configure(text="     A 2004 by Aouizerate, et al.¹¹ showed that the orbitofrontal cortex (OFC), the anterior cingulate cortex (ACC), the dorsolateral prefrontal cortex (DLPC), the head of the caudate nucleus and the thalamus are all associated with OCD.\n\n"
                                  "     The OFC is involved in the creating significance that is attributed to the consequences of action, which thereby leads to decision-making.\n"
                                  "The ACC is particularly activated in situations in which there are conflicting options and a high likelihood of making an error.\n"
                                  "The DLPC plays in important part in processing relevant information. This information is integrated by the caudate nucleus, which controls behavioral programs. Dysfunction in these networks \"will result in the emergence and maintenance of repetitive thoughts and characteristic OCD behavior\".\n\n"
                                  "     Based on this data, it looks like OCD is caused by the dysregulation of parts of the brain that process and attribute significance to information, which affects their behavioral programs in the forms of compulsions.")
        mb_psycho(1)
    else:
        mb_psycho(0)

########################################################################################################################
########################################################################################################################
################################ main ##################################################################################
window = Tk()
xd = 1920
yd = 1080
window.geometry("1920x1080")
window.title("Physiology Term Project")
window.attributes('-fullscreen', True)
# window.wm_attributes('-transparentcolor', '#ab23ff')
# window.configure(bg='#ffffff')

canvas = Canvas(window, width=xd, height=yd)
canvas.create_rectangle(xd / 4, -1, (xd / 4) + 50, yd + 1, fill='grey')
canvas.pack()


start = Frame(window, width=(xd / 4), height=yd)
start.pack()

start.place(x=0, y=0)

start_b = Label(start, text="Welcome to the \n Interactive Brain Program \n\n PSY355: Physiological Psychology \n "
                            "Created by Julian Westerlund", fg="Black", font=("Lucida Sans", 20))
start_b.pack(side=TOP, pady=15)

begin = Button(start, text="Begin", fg="white", bg="#00FF00", font=("Lucida Sans", 25), width=7,
               command=lambda: [destroy([start]), show(sb, 0, 0), show(home_b, 13, 871), show(back_b, 253, 871), home(1)])
begin.pack(pady=20)

gif = ImageLabel(window)
gif.load('pics/brain.gif')
gif.place(x=(xd / 4) + 145, y=(yd / 3) - 150)

back_b = Button(window, text="Back", bg="black", fg="white", height=2, width=17, font=('Lucida Sans', 14), command=back)
home_b = Button(window, text="Restart", bg="black", fg="white", height=2, width=17, font=('Lucida Sans', 14), command=restart)
help_b = Button(window, text="Help", bg="#98e7ff", fg="Black", height=2, width=37, font=('Lucida Sans', 15), command=help)
show(help_b, 13, 940)
exit = Button(window, text="Quit", bg="red", fg="white", height=2, width=37, font=('Lucida Sans', 15),
              command=window.destroy)
exit.place(x=13, y=1010)

########################################################################################################################

global history
history = [home]

################################ IMAGES ################################################################################

sections_of_the_brain = ImageTk.PhotoImage(Image.open("pics/sec_brain.png"), master=window)
hindbrain_p = ImageTk.PhotoImage(Image.open("pics/hindbrain_midbrain.png"), master=window)
midbrain_p = ImageTk.PhotoImage(Image.open("pics/hindbrain.png"), master=window)
forebrain_p = ImageTk.PhotoImage(Image.open("pics/lobes.png"), master=window)
limbic_p = ImageTk.PhotoImage(Image.open("pics/limbic.png"), master=window)

neuron_p = ImageTk.PhotoImage(Image.open("pics/neuron2.png"))

############################# home #####################################################################################
sb = Frame(window, width=xd / 4, height=yd)
sb.pack()

title = Label(sb, text="", justify=LEFT, anchor=W, font=("Lucida Sans", 30), pady=30)
title.pack(side=TOP)

body = Label(sb, text="", justify=LEFT, anchor=W, font=("Lucida Sans", 20), wraplength=450, width=26)
body.pack(side=TOP, padx=15)

brain_b = Button(sb, text="The Brain", bg="gray", fg="black", height=3, width=20, font=('Lucida Sans', 20),
                     command=lambda: [show(gif, x=2000, y=0), hide([psycho_b, neuron_b, brain_b]), show(mb, (xd / 4) + 51, 0),
                                      brain(1)])
neuron_b = Button(sb, text="The Neuron", bg="gray", fg="black", height=3, width=20, font=('Lucida Sans', 20),
                      command=lambda: [show(gif, x=2000, y=0), hide([psycho_b, neuron_b, brain_b]), show(mb, (xd / 4) + 51, 0),
                                       neuron(1)])
psycho_b = Button(sb, text="Psychopathology", bg="gray", fg="black", height=3, width=20, font=('Lucida Sans', 20),
                      command=lambda: [show(gif, x=2000, y=0), hide([psycho_b, neuron_b, brain_b]), show(mb, (xd / 4) + 51, 0),
                                       psycho(1)])

mb = Frame(window, width=3*(xd / 4)-51, height=yd)
lobes_pic = Label(mb, image=sections_of_the_brain)
forebrain_pic = Label(mb, image=forebrain_p)
hindbrain_pic = Label(mb, image=hindbrain_p)
midbrain_pic = Label(mb, image=midbrain_p)
limbic_pic = Label(mb, image=limbic_p)
neuron_pic = Label(mb, image=neuron_p)

########################################################################################################################
############ sbar ######################################################################################################
def sbar(t,b):
    title.configure(text=t)
    body.configure(text=b)
########################################### BRAIN ######################################################################


hind_and_midbrain_b = Button(mb, text="The Midbrain and Hindbrain", bg="#8e75d8", fg="white", height=2, font=('Lucida Sans', 20), command=lambda: [brain(0), hind_and_midbrain(1)])
forebrain_b = Button(mb, text="The Cerebral Cortex", bg="#e889ab", fg="black", height=2, width=17, font=('Lucida Sans', 20), command=lambda: [brain(0), forebrain(1)])
limbic_b = Button(mb, text="The Limbic System", bg="#e889ab", fg="black", height=2, width=15, font=('Lucida Sans', 20), command=lambda: [brain(0), limbic(1)])
#---------------------------------------forebrain
occipital_b = Button(mb, text="Occipital Lobe", bg="#f7a8b7", fg="black", height=3, width=15, font=('Lucida Sans', 20), command = lambda: [sbar("Occipital Lobe", "The occipital lobe (located on the posterior end of the cortex) is "
                                                                                                                                                                  "responsible for the processing of vision. This includes"
                                                                                                                                                                  " the movement of objects, and object recognition.")])

parietal_b = Button(mb, text="Parietal Lobe", bg="#fcfb99", fg="black", height=3, width=15, font=('Lucida Sans', 20), command = lambda: [sbar("Parietal Lobe", "The parietal lobe (located on the dorsal side of the cortex) is responsible "
                                                                                                                                                               "for the receiving touch information from the rest of the body and detecting the "
                                                                                                                                                               "body's spacial orientation.")])
frontal_b = Button(mb, text="Frontal Lobe", bg="#b5d9ed", fg="black", height=3, width=15, font=('Lucida Sans', 20), command = lambda: [sbar("Frontal Lobe", "The frontal lobe (located on the anterior end of the cortex) consists of two main parts: "
                                                                                                                                                            "the primary motor cortex, and the prefrontal cortex.\n\nThe primary motor cortex is responsible for controlling the"
                                                                                                                                                            " body's motor movements. \n\nThe prefrontal cortex is responsible for our cognitive executive functions, which allow us to"
                                                                                                                                                            " focus our attention, make mental notes (working memory), and make complex decisions.")])
temporal_b = Button(mb, text="Temporal Lobe", bg="#b7d09e", fg="black", height=3, width=15, font=('Lucida Sans', 20), command = lambda: [sbar("Temporal Lobe", "The temporal lobe (located laterally to the temples) is responsible for the processing of "
                                                                                                                                                               "auditory info, which includes speech comprehension, and complex visual aspects of vision, such as face recognition.")])
#---------------------------------------limbic system
thalamus_b = Button(mb, text="Thalamus", bg="#d45a45", fg="White", height=2, width=15, font=('Lucida Sans', 20), command = lambda: [sbar("Thalamus", "The thalamus (located in the center of the forebrain) is the sensory relay station for the brain. "
                                                                                                                                                     "It receives input from all sensory organs of the body (except for olfaction) and outputs it to the cerebral cortex. "
                                                                                                                                                     "Some signals from the cerebral cortex are sent back to the thalamus for amplification.")])
hypothalamus_b = Button(mb, text="Hypothalamus", bg="#42934b", fg="White", height=2, width=15, font=('Lucida Sans', 20), command = lambda: [sbar("Hypothalamus", "The hypothalamus (located ventral to the thalamus and at the base of the brain) receives input from the thalamus"
                                                                                                                                                                 " and sends signals to the pituitary gland to release hormones to the rest of the body.\n\n"
                                                                                                                                                                 "These hormones activate feelings of hunger, thirst, sexual arousal, and aggression, and help regulate body temperature and activity level.")])
hippocampus_b = Button(mb, text="Hippocampus", bg="#d76f80", fg="White", height=2, width=15, font=('Lucida Sans', 20), command = lambda: [sbar("Hippocampus", "The hippocampus (located between the thalamus and the posterior end of the cerebral cortex) is primarily responsible for the storage of "
                                                                                                                                                              "declarative memory (especially episodic memory) and specific locations.")])
amygdala_b = Button(mb, text="Amygdala", bg="#516b9d", fg="White", height=2, width=15, font=('Lucida Sans', 20), command = lambda: [sbar("Amygdala", "The amygdala (located anterior to the hippocampus) is responsible for "
                                                                                                                                                     "the processing of fearful and threatening stimuli.⁵\n\n"
                                                                                                                                                     "It receives sensory input and designates it as threatening or not and stores it's designation in memory.")])
cingulate_b = Button(mb, text="Cingulate Gyrus", bg="#d56054", fg="White", height=2, width=15, font=('Lucida Sans', 20), command=lambda: [sbar("Cingulate Gyrus", "The cingulate gyrus is responsible for processing emotions and regulating behaviors. "
                                                                                                                                                                  "It has many connections to the frontal, temporal, and occipital cortices on both sides of the brain.⁶ "
                                                                                                                                                                  "It coordinates sensory input with emotion, provides emotional responses to pain, and is important for decision making.")])
#----------------------------------------hindbrain
pons_b = Button(mb, text="Pons", bg="#ffa673", fg="white", height=1, width=13, font=('Lucida Sans', 23), command = lambda: [sbar("Pons", "The pons (which is anterior and ventral to the medulla) is the location where axons switch to the opposite side of the body.")])
cerebellum_b = Button(mb, text="Cerebellum", bg="#feb674", fg="white", height=1, width=15, font=('Lucida Sans', 20), command = lambda: [sbar("Cerebellum", "The cerebellum (located in the back of the head) controls balance and coordination, and shifts attention"
                                                                                                                                                           " between auditory and visual stimuli. It is also crucial for keeping a steady rhythm.")])
medulla_b = Button(mb, text="Medulla", bg="#ffa673", fg="White", height=1, width=15, font=('Lucida Sans', 20), command = lambda: [sbar("Medulla", "The medulla (located above the spinal cord) connects the head and organs and is important for breathing, heart rate,"
                                                                                                                                                  " vomiting, salivation, coughing, and breathing.")])
spinalc_b = Button(mb, text="Spinal Cord", bg="#ffa673", fg="White", height=1, width=15, font=('Lucida Sans', 20), command = lambda: [sbar("Spinal Cord", "The spinal cord (begins at the brain stem and ends in the lower back) is an extension of the central nervous system and "
                                                                                                                                                          "transports sensory information to and from the periphery, and outputs motor movements.")])
#----------------------------------------midbrain
tectum_b = Button(mb, text="Tectum", bg="#69ddc8", fg="White", height=1, width=15, font=('Lucida Sans', 20), command = lambda: [sbar("Tectum", "The tectum is the roof of the midbrain and is partially responsible for reflexes in response to auditory or visual stimuli.⁹")])
colliculus_b = Button(mb, text="Colliculus", bg="#69ddc8", fg="White", height=1, width=15, font=('Lucida Sans', 20), command = lambda: [sbar("Colliculus", "The colliculus consists of two parts, the inferior and superior colliculus.\n\n"
                                                                                                                                                           "The inferior colliculus processes auditory information and the superior colliculus processes visual information.")])
tegmentum_b = Button(mb, text="Tegmentum", bg="#69ddc8", fg="White", height=1, width=15, font=('Lucida Sans', 20), command = lambda: [sbar("Tegmentum", "The tegmentum is ventral to the tectum and covers it.")])
nigra_b = Button(mb, text="Substantia Nigra", bg="black", fg="White", height=2, width=15, font=('Lucida Sans', 20), command = lambda: [sbar("Substantia Nigra", "The substantia nigra, which is part of the basal ganglia, is part of the dopamine-containing pathways that facilitates readiness for movement.")])
#########################################################################################################################
############################### NEURON ##################################################################################
soma_b = Button(mb, text="Soma (Cell Body)", bg="#ff9e6b", fg="Black", height=3, width=15, font=('Lucida Sans', 20), command = lambda: [sbar("Soma", "The soma contains structures important for supporting the chemical processes of the neuron, like the production of neurotransmitters.\n\n"
                                                                                                                                                     "These structures include the nucleus, ribosomes, mitochondria, endoplasmic reticulum, lysosomes, and the golgi complex.")])
dendrites_b = Button(mb, text="Dendrites", bg="#ff6600", fg="White", height=3, width=15, font=('Lucida Sans', 20), command = lambda: [sbar("Dendrites", "Dendrites are branching fibers that receive signals from the axons of neighbouring neurons.\n\n"
                                                                                                                                                        "They are lined with synaptic receptors that detect the presence of neurotransmitters which facilitate the creation of action potentials.")])
axon_b = Button(mb, text="Axon", bg="#ffdd55", fg="#800000", height=3, width=15, font=('Lucida Sans', 20), command = lambda: [sbar("Axon", "The axon is a thin fiber of constant diameter which sends signals to the neurons of other organs or muscles.\n\n"
                                                                                                                                           "Axons are surrounded in a fatty insulating material called the Myelin Sheath with allows for the faster transmission of action potentials.")])
synapse_b = Button(mb, text="Synapse", bg="#ff6600", fg="white", height=3, width=15, font=('Lucida Sans', 20), command = lambda: [sbar("Synapse", "The synapse is a gap between the axon and dendrite where neurotransmitters are released.\n\n"
                                                                                                                                                  "There are many types of neurotransmitters such as dopamine, seratonin, glutamate, GABA, acetylcholine, and epinephrine.")])
#################PSYCHOPATHOLOGY #########################################################################################
depression_b = Button(sb, text="Depression", bg="Black", fg="White", height=2, width=15, font=('Lucida Sans', 20), command = lambda: [depression(1)])
anxiety_b = Button(sb, text="Anxiety", bg="Black", fg="White", height=2, width=15, font=('Lucida Sans', 20), command = lambda: [anxiety(1)])
adhd_b = Button(sb, text="ADHD", bg="Black", fg="White", height=2, width=15, font=('Lucida Sans', 20), command = lambda: [adhd(1)])
schizo_b = Button(sb, text="Schizophrenia", bg="Black", fg="White", height=2, width=15, font=('Lucida Sans', 20), command = lambda: [schizophrenia(1)])
ocd_b = Button(sb, text="OCD", bg="Black", fg="White", height=2, width=15, font=('Lucida Sans', 20), command = lambda: [ocd(1)])

title_path = Label(mb, justify="left", font=('Lucida Sans', 30))
sym_path = Label(mb, wraplength=600, justify="left", font=('Lucida Sans', 17))
neuro_path = Label(mb, wraplength=600, justify="left", font=('Lucida Sans', 17))
sym_t_path = Label(mb, justify="left", font=('Lucida Sans', 20), text="Psychological Symptoms:")
neuro_t_path = Label(mb, justify="left", font=('Lucida Sans', 20), text="Neuropsychology:")
########################################################################################################################

def update_coords(obj, xc, yc, wv, hv, fv):
    obj.configure(width=wv, height=hv, font=('Lucida Sans', fv))
    obj.place(x=xc, y=yc)
    print(xc, yc, wv, hv, fv)

def motion(self): #works
    x = window.winfo_pointerx()
    y = window.winfo_pointery()
    mousecoords.configure(text='{}, {}'.format(x, y))

def debug_move(obj):
    obj.place(x=window.winfo_pointerx(), y=window.winfo_pointery())
    y.delete(0, END)
    x.delete(0, END)
    x.insert(0, str(window.winfo_pointerx()))
    y.insert(0, str(window.winfo_pointery()))

def print_location(self):
    print("x="+str(widget.winfo_rootx()-512)+", y="+str(widget.winfo_rooty()))

def open_debugger(self): #only works for buttons, if you want to do other stuff, you have to make try-catch for attributes such as width, depth, etc.
    root = Toplevel(window)
    root.title("Style Debugger")

    global widget
    #widget = forebrain_b ######################################## INPUT

    fontsize = widget.cget('font').split()[2]

    debug = tk.Frame(root, width=500, height=500)
    debug.pack()

    global x
    x = tk.Entry(debug)
    x.insert(0, widget.winfo_rootx())
    x.grid(row=0, column=1, pady=5, padx=4)

    xl = tk.Label(debug, text="X-Coordinate:") #xl = x-label
    xl.grid(row=0, column=0, padx=1)

    global y
    y = tk.Entry(debug)
    y.insert(0, widget.winfo_rooty())
    y.grid(row=1, column=1, pady=5, padx=4)

    yl = tk.Label(debug, text="Y-Coordinate:")
    yl.grid(row=1, column=0, padx=1)

    w = tk.Entry(debug)
    w.insert(0, widget.cget("width"))
    w.grid(row=2, column=1, pady=5, padx=4)

    wl = tk.Label(debug, text="Width:")
    wl.grid(row=2, column=0, padx=1)

    h = tk.Entry(debug)
    h.insert(0, widget.cget("height"))
    h.grid(row=3, column=1, pady=5, padx=4)

    hl = tk.Label(debug, text="Height:")
    hl.grid(row=3, column=0, padx=1)

    f = tk.Entry(debug)
    f.insert(0, fontsize)
    f.grid(row=4, column=1, pady=5, padx=4)

    fl = tk.Label(debug, text="Font Size")
    fl.grid(row=4, column=0, padx=1)

    update = Button(debug, text="Update", font=(15), command=lambda : update_coords(widget, int(x.get()), int(y.get()), int(w.get()), int(h.get()), int(f.get())))
    update.grid(row=2, column=2, padx=4)

    print(int(x.get()), int(y.get()), int(w.get()), int(h.get()), int(f.get()))

    x_pos = window.winfo_pointerx()
    y_pos = window.winfo_pointery()

    global mousecoords
    mousecoords = Label(debug, text='{}, {}'.format(x_pos, y_pos))
    mousecoords.grid(row=5, column=1)

    window.bind('<Motion>', motion)
    root.mainloop()

global widget
widget = pons_b

    #Label(mb, text="Major Depressive Disorder", justify="left", font=('Lucida Sans', 25))

#widget = Button(mb, text="Test Button", bg='Black', fg="White", width="15", height="2",font=('Lucida Sans', 20))
#widget3 = midbrain_pic
#widget2 = hindbrain_pic

window.bind('<Control-s>', lambda event, widget=widget: debug_move(widget))
#window.bind('<Control-w>', lambda event, widget=widget: debug_move(widget2))
window.bind('<Control-d>', open_debugger)
window.bind('<Control-a>', print_location)
window.mainloop()