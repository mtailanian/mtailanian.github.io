---
title:
layout: default
permalink: /phd/
published: true
---


# Deep Image Generative Modeling and Statistical Testing for Industrial Anomaly Detection


## Defensa Doctorado Matías Tailanian

Tutores:
* Pablo Musé
* Álvaro Pardo

Tribunal:
* Matías Di Martino
* Thibaud Ehret
* Jean-Michel Morel
* Gregory Randall

### Coordenadas

Fecha: Martes 17 de setiembre, 8h @ Uruguay

Lugar:

- Facultad de Ingeniería, salón 705 (piso 7, cuerpo central). Habrá un brindis a continuación en Instituto de Ingeniería Eléctrica.

- Zoom : 

    - https://salavirtual-udelar.zoom.us/j/2165307614?pwd=c1EvSnlUUFg0TDlKUDVRd3lKOG01Zz09
    - Meeting ID: 216 530 7614
    - Passcode: pwd-AB2021

## Resumen

This thesis addresses the challenge of anomaly detection in images, for industrial applications. It explores advanced methodologies employing both classical image processing techniques and modern generative modeling approaches, specifically focusing on Normalizing Flows and Diffusion Models.


As anomalies are rare by definition, collecting normal samples is generally easier and more feasible in industrial settings than acquiring comprehensive datasets with labeled anomalies. Therefore, the focus of this research is on unsupervised methods, and one-class methods, where the idea is to model the "normality" and detect anomalies as everything that deviates from this model.


Initially, a multi-scale anomaly detection method based on classical image processing techniques is proposed, leveraging an a contrario approach to control the number of false alarms. Subsequently, a novel method called U-Flow is introduced, which employs a U-shaped architecture in Normalizing Flows to achieve anomaly detection with automatic thresholding. Then, this thesis further explores the use of Diffusion Models for anomaly detection, presenting the Diffusion Anomaly Detection (DAD) method. This work incorporates score-based generative models and inpainting techniques to refine anomaly detection capabilities. Additionally, a new diffusion-based method called RIFA (Random Inpainting For Anomaly detection) is proposed as a completely unsupervised alternative. Finally, the techniques and knowledge gained from Diffusion Models are applied to a completely different application: counter-forensics.


Throughout the whole thesis, a special emphasis is placed on bridging the gap between theoretical research and practical industrial applications, setting the theoretical foundations for obtaining automatic segmentations of anomalies, by performing statistical tests and controlling the number of false alarms using the a contrario framework.


Experimental results on standard datasets validate the effectiveness of the proposed methods, highlighting substantial performance gains in some cases. The final chapter applies the best-performing method to two industrial problems: quality control in manufacturing leather samples for the upholstery industry, and defect detection in fruits, demonstrating its practical viability and impact on improving quality control processes in these industries.


In addition, this research contributes to the open-source community with several code repositories and has resulted in four published papers so far, and hopefully, more will follow. Future work will particularly focus on improving likelihood estimation with Diffusion Models and expanding its applicability to other industrial domains.