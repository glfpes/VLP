Skipping 'm', missing information
Skipping 'l', missing information
Skipping 'o', missing information
Skipping 'n', missing information
[1m[37mStarting: Aoa full on image ./jason.jpg taken with <module 'phones.cameras.jason_back' from 'C:\Users\glfpes\Desktop\vlc\project\vlc\vlc-localization-master\vlc-localization-master\processing\phones\cameras\jason_back.pyc'> in <module 'rooms.jason' from 'C:\Users\glfpes\Desktop\vlc\project\vlc\vlc-localization-master\vlc-localization-master\processing\rooms\jason.pyc'>[0m
[34m    Transmitter frequencies = [2000 3000 3500 2500 4000][0m
[1m[30m    Starting: Process image ./jason.jpg with 0 transmitter(s) taken with <module 'phones.cameras.jason_back' from 'C:\Users\glfpes\Desktop\vlc\project\vlc\vlc-localization-master\vlc-localization-master\processing\phones\cameras\jason_back.pyc'>[0m
[1m[30m        Starting: Loading image[0m
[34m            gray_image.shape = (3072, 1728)[0m
[34m            Saved WIP to /tmp/luxp-opencv_fft-step1-gray_image.png[0m
[1m[30m        Complete: Loading image (0.144 secs)[0m
[1m[30m        Starting: Normalizing image rotation[0m
[34m            Saved WIP to /tmp/luxp-opencv_fft-step2-gray_image_rotated.png[0m
[34m            gray_image.shape = (3072, 1728)[0m
[1m[30m        Complete: Normalizing image rotation (0.091 secs)[0m
[1m[30m        Starting: Applying blur[0m
[34m            Saved WIP to /tmp/luxp-opencv_fft-step3-after_blur.png[0m
[34m            m2.shape = (3072, 1728)[0m
[1m[30m        Complete: Applying blur (0.044 secs)[0m
[1m[30m        Starting: Threshold image[0m
[34m            Saved WIP to /tmp/luxp-opencv_fft-step4-thresholded_img.png[0m
[1m[30m        Complete: Threshold image (0.038 secs)[0m
[1m[30m        Starting: Locate transmitters[0m
[34m            heirarchy = [[[ 1 -1 -1 -1]
              [ 2  0 -1 -1]
              [ 3  1 -1 -1]
              [ 4  2 -1 -1]
              [-1  3 -1 -1]]][0m
[34m            Saved WIP to /tmp/luxp-opencv_fft-step5-contours.png[0m
[34m            Transmitter at (2016, 1494). Radius of 50 pixels[0m
[34m            Transmitter area 7853.98163397. Contour area 6658.5. %age 84.7786550862[0m
[34m            Transmitter at (1990, 378). Radius of 42 pixels[0m
[34m            Transmitter area 5541.76944093. Contour area 4915.5. %age 88.6991068898[0m
[34m            Transmitter at (1456, 896). Radius of 37 pixels[0m
[34m            Transmitter area 4300.84034276. Contour area 3906.0. %age 90.8194605868[0m
[34m            Transmitter at (1028, 469). Radius of 28 pixels[0m
[34m            Transmitter area 2463.00864041. Contour area 1848.0. %age 75.0301874576[0m
[34m            Transmitter at (1013, 1390). Radius of 26 pixels[0m
[34m            Transmitter area 2123.71663383. Contour area 1763.0. %age 83.0148416186[0m
[34m            Saved WIP to /tmp/luxp-opencv_fft-step6-contours-kept.png[0m
[1m[30m        Complete: Locate transmitters (0.208 secs)[0m
[1m[30m        Starting: Computing transmitter frequencies[0m
[34m            peaks =
            [ 10  55  88  98 109 162 198 217 241 267 324 359 389 431 455 485][0m
[34m            f[peaks] =
            [  185.546875   1020.5078125  1632.8125     1818.359375   2022.4609375
              3005.859375   3673.828125   4026.3671875  4471.6796875  4954.1015625
              6011.71875    6661.1328125  7217.7734375  7997.0703125  8442.3828125
              8999.0234375][0m
[34m            Y_plot[peaks] =
            [ 3815.66804916   298.44130945    83.87766673    53.09147382    68.07053227
              6655.87121929    67.73119797   155.63388189    56.16626281   202.14951404
               793.40386867    95.10603197   124.05544466    98.7296551     82.07280311
              1779.59525717][0m
[34m            center (2015, 1493) peak_freq = 3005.859375[0m
[34m            peaks =
            [ 11  42  57  76 112 140 188 231 249 273 292 356 393 421 459 494][0m
[34m            f[peaks] =
            [  204.1015625   779.296875   1057.6171875  1410.15625    2078.125
              2597.65625    3488.28125    4286.1328125  4620.1171875  5065.4296875
              5417.96875    6605.46875    7291.9921875  7811.5234375  8516.6015625
              9166.015625 ][0m
[34m            Y_plot[peaks] =
            [ 3020.0899068    123.56141339   106.56659813   184.33084562   168.48300915
               151.46981563  5583.81960575    24.13872396    72.43170029   128.72140061
                43.50840018   163.20471666   153.05493808    43.25261083  1320.09455179
                56.33552399][0m
[34m            center (1989, 378) peak_freq = 3488.28125[0m
[34m            peaks =
            [ 13  89 110 129 212 253 286 316 348 388 425 450 494][0m
[34m            f[peaks] =
            [  241.2109375  1651.3671875  2041.015625   2393.5546875  3933.59375
              4694.3359375  5306.640625   5863.28125    6457.03125    7199.21875
              7885.7421875  8349.609375   9166.015625 ][0m
[34m            Y_plot[peaks] =
            [ 1956.90056956   111.24571933   120.04894397   149.81803332  4538.2644628
               161.59152145    77.0767282    131.71711517    52.97338252  1045.63045917
                82.02989498   117.17675221    42.46308214][0m
[34m            center (1459, 896) peak_freq = 3933.59375[0m
[34m            peaks =
            [ 17 109 180 203 245 328 376 433 479][0m
[34m            f[peaks] =
            [  315.4296875  2022.4609375  3339.84375    3766.6015625  4545.8984375
              6085.9375     6976.5625     8034.1796875  8887.6953125][0m
[34m            Y_plot[peaks] =
            [ 1322.57386741  2935.23402203    44.76793742    31.59288981   160.71521328
              1028.14447366   143.45527435   220.36301117   346.99874171][0m
[34m            center (1030, 470) peak_freq = 2022.4609375[0m
[34m            peaks =
            [ 16  65 135 209 268 345 407 482][0m
[34m            f[peaks] =
            [  296.875      1206.0546875  2504.8828125  3877.9296875  4972.65625
              6401.3671875  7551.7578125  8943.359375 ][0m
[34m            Y_plot[peaks] =
            [  829.47976903   100.3686188   2804.98472592   158.93846694   210.55711033
               207.82588047   785.62435982   293.34442622][0m
[34m            center (1016, 1390) peak_freq = 2504.8828125[0m
[1m[30m            Starting: plot_subplots for freq_fft_transmitters[0m
[34m                Plotted WIP subplots to /tmp/luxp-opencv_fft-step7-freq_fft_transmitters.png[0m
[1m[30m            Complete: plot_subplots for freq_fft_transmitters (1.053 secs)[0m
[34m            Saved WIP to /tmp/luxp-opencv_fft-step8-contours-kept-labeled.png[0m
[34m            Saved WIP to /tmp/luxp-opencv_fft-step9-circles.png[0m
[34m            estimated_frequencies = [3005.859375, 3488.28125, 3933.59375, 2022.4609375, 2504.8828125][0m
[1m[30m        Complete: Computing transmitter frequencies (1.810 secs)[0m
[1m[30m    Complete: Process image ./jason.jpg with 0 transmitter(s) taken with <module 'phones.cameras.jason_back' from 'C:\Users\glfpes\Desktop\vlc\project\vlc\vlc-localization-master\vlc-localization-master\processing\phones\cameras\jason_back.pyc'> (2.339 secs)[0m
[34m    Translated light center points: [[-479 -629]  [-453  486]  [  77  -32]  [ 506  394]  [ 520 -526]][0m
[34m    Original frequencies: [ 3005.859375   3488.28125    3933.59375    2022.4609375  2504.8828125][0m
[34m      Actual frequencies: [3000, 3500, 4000, 2000, 2500][0m
[34m    Raw lights information: [(array([-479, -629]), ((5, -5, 0),)), (array([-453,  486]), ((-5, -5, 0),)), (array([ 77, -32]), ((0, 0, 0),)), (array([506, 394]), ((-5, 5, 0),)), (array([ 520, -526]), ((5, 5, 0),))][0m
[1m[30m    Starting: AoA on lights [(array([-479, -629]), (5, -5, 0)), (array([-453,  486]), (-5, -5, 0)), (array([ 77, -32]), (0, 0, 0)), (array([506, 394]), (-5, 5, 0)), (array([ 520, -526]), (5, 5, 0))] with Zf=2271[0m
[34m        centers
        [[-479 -629]
         [-453  486]
         [  77  -32]
         [ 506  394]
         [ 520 -526]][0m
[34m        transmitters
        [[ 5 -5  0]
         [-5 -5  0]
         [ 0  0  0]
         [-5  5  0]
         [ 5  5  0]][0m
[34m        centers
        [[ -479.  -629.  2271.]
         [ -453.   486.  2271.]
         [   77.   -32.  2271.]
         [  506.   394.  2271.]
         [  520.  -526.  2271.]][0m
[1m[30m        Starting: Pre-computing static arrays used for AoA[0m
[34m            image_squared_distance
            [ 5782523.  5598846.  5164394.  5568713.  5704517.][0m
[34m            transmitter_pair_squared_distance
            [[   0.  100.   50.  200.  100.]
             [   0.    0.   50.  100.  200.]
             [   0.    0.    0.   50.   50.]
             [   0.    0.    0.    0.  100.]][0m
[34m            pairwise_image_inner_products
            [[       0.  5068734.  5140686.  4667241.  5239215.]
             [       0.        0.  5107008.  5119707.  4666245.]
             [       0.        0.        0.  5183795.  5214313.]
             [       0.        0.        0.        0.  5213317.]][0m
[1m[30m        Complete: Pre-computing static arrays used for AoA (0.002 secs)[0m
[1m[30m        Starting: Minimize distance function[0m
[-0.2, -0.2, -0.2, -0.2, -0.2] (k_vals_init from static)
[-0.00869158 -0.00937414 -0.00935886 -0.0105952  -0.01031027] (k_vals after leastsq)
[34m            k_vals = [-0.00869158 -0.00937414 -0.00935886 -0.0105952  -0.01031027][0m
[1m[30m        Complete: Minimize distance function (0.006 secs)[0m
[1m[30m        Starting: Minimize location function[0m
[34m            rx_location = [  1.84745784  -7.56762042  20.53919299][0m
[1m[30m        Complete: Minimize location function (0.002 secs)[0m
[34m        absolute_centers =
        [[  4.16326733   4.24648626  -0.72063227  -5.36117125  -5.36133852]
         [  5.46700449  -4.55583294   0.29948354  -4.17450884   5.42320012]
         [-19.73858061 -21.28867614 -21.25397241 -24.06169944 -23.41461498]][0m
[1m[30m        Starting: Minimize rotation function[0m
[34m            rx_rotation =
            [[-0.01863158  1.00684616  0.10803855]
             [-0.94003163  0.02924448 -0.31850183]
             [-0.3063633  -0.09365667  0.94619398]][0m
[1m[30m        Complete: Minimize rotation function (0.003 secs)[0m
[1m[30m        Starting: Compute error[0m
[34m            rx_location_error = 0.0311202773036[0m
[1m[30m        Complete: Compute error (0.000 secs)[0m
[1m[30m    Complete: AoA on lights [(array([-479, -629]), (5, -5, 0)), (array([-453,  486]), (-5, -5, 0)), (array([ 77, -32]), (0, 0, 0)), (array([506, 394]), (-5, 5, 0)), (array([ 520, -526]), (5, 5, 0))] with Zf=2271 (0.017 secs)[0m
[1m[32m    location estimate = [  1.84745784  -7.56762042  20.53919299][0m
[1m[32m    location error    = 0.0311202773036[0m
[1m[37mComplete: Aoa full on image ./jason.jpg taken with <module 'phones.cameras.jason_back' from 'C:\Users\glfpes\Desktop\vlc\project\vlc\vlc-localization-master\vlc-localization-master\processing\phones\cameras\jason_back.pyc'> in <module 'rooms.jason' from 'C:\Users\glfpes\Desktop\vlc\project\vlc\vlc-localization-master\vlc-localization-master\processing\rooms\jason.pyc'> (2.362 secs)[0m
[1m[32mrx_location = [  1.84745784  -7.56762042  20.53919299][0m
[1m[32mrx_rotation =
[[-0.01863158  1.00684616  0.10803855]
 [-0.94003163  0.02924448 -0.31850183]
 [-0.3063633  -0.09365667  0.94619398]][0m
[1m[32mlocation_error = 0.0311202773036[0m
