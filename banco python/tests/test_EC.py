import pytest
import sys

sys.path.append("C:\\Users\\thier\\SoftwareTests\\banco python\\src")
from main import banco

D9_CEM_ELEMENTOS = [(0, 1), (1, 5), (4, 1), (7, 6), (9, 7), (13, 6), (14, 3), (15, 7), (20, 3), (21, 6), (22, 5), (28, 4), (29, 4), (31, 6), (36, 4), (41, 2), (55, 8), (57, 5), (60, 2), (63, 9), (65, 8), (66, 8), (66, 2), (66, 1), (72, 2), (78, 9), (85, 9), (85, 6), (87, 4), (88, 9), (90, 1), (92, 8), (92, 7), (93, 8), (96, 4), (97, 7), (102, 8), (103, 9), (104, 2), (111, 5), (112, 2), (112, 4), (114, 3), (115, 6), (115, 8), (117, 8), (120, 6), (120, 4), (124, 6), (124, 4), (131, 1), (132, 6), (133, 4), (134, 3), (135, 6), (135, 9),
                    (138, 7), (149, 5), (150, 1), (150, 8), (151, 3), (151, 3), (155, 7), (158, 3), (160, 4), (164, 2), (166, 1), (167, 9), (167, 4), (171, 8), (173, 3), (175, 8), (176, 2), (179, 6), (179, 4), (183, 3), (186, 9), (187, 4), (188, 5), (189, 9), (191, 3), (192, 1), (199, 4), (200, 9), (204, 9), (208, 6), (208, 3), (211, 6), (214, 4), (217, 7), (219, 1), (222, 3), (222, 2), (225, 9), (226, 3), (226, 4), (234, 9), (238, 1), (240, 7), (245, 5)]

D10_CEM_ELEMENTOS = [(0, 10)] + D9_CEM_ELEMENTOS[1:]

D9_SEISCENTOS_ELEMENTOS = [(0, 5), (8, 5), (9, 1), (10, 8), (10, 8), (10, 6), (11, 4), (11, 6), (12, 5), (12, 7), (13, 6), (13, 2), (14, 4), (14, 9), (15, 9), (15, 1), (16, 1), (16, 3), (16, 3), (17, 3), (17, 7), (17, 5), (17, 9), (18, 4), (18, 9), (18, 5), (20, 4), (20, 5), (20, 3), (20, 8), (21, 6), (21, 2), (21, 2), (21, 8), (21, 8), (21, 1), (21, 8), (22, 7), (23, 6), (24, 9), (24, 2), (25, 4), (25, 3), (25, 3), (25, 4), (26, 9), (26, 6), (26, 7), (26, 7), (26, 7), (27, 7), (27, 8), (27, 3), (28, 3), (28, 6), (28, 3), (29, 9), (29, 3), (30, 2), (30, 4), (30, 8), (31, 8), (32, 7), (32, 6), (32, 2), (33, 8), (33, 6), (33, 9), (34, 6), (34, 3), (34, 8), (35, 7), (35, 1), (36, 5), (36, 5), (36, 1), (37, 5), (37, 7), (37, 4), (38, 1), (38, 9), (40, 1), (40, 8), (41, 9), (42, 5), (42, 9), (43, 4), (43, 5), (44, 6), (44, 1), (44, 3), (45, 5), (45, 9), (46, 4), (47, 7), (47, 8), (47, 8), (47, 1), (48, 9), (48, 8), (48, 6), (48, 5), (48, 1), (48, 4), (49, 6), (49, 4), (49, 9), (49, 5), (50, 8), (50,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              1), (50, 4), (50, 7), (51, 6), (51, 4), (51, 7), (52, 8), (52, 8), (52, 1), (53, 7), (54, 1), (54, 1), (54, 1), (55, 6), (56, 1), (56, 5), (56, 2), (57, 2), (57, 4), (57, 8), (58, 7), (58, 4), (59, 5), (59, 9), (60, 3), (60, 7), (62, 6), (62, 4), (63, 7), (63, 4), (63, 7), (63, 9), (64, 8), (64, 9), (65, 9), (66, 3), (66, 8), (66, 5), (67, 8), (67, 7), (67, 9), (68, 2), (68, 6), (68, 7), (69, 7), (69, 2), (71, 8), (71, 4), (72, 9), (72, 9), (73, 1), (73, 2), (73, 2), (74, 2), (75, 6), (76, 9), (77, 7), (77, 2), (77, 6), (77, 4), (78, 3), (79, 6), (80, 1), (80, 2), (81, 3), (81, 7), (81, 9), (81, 3), (81, 6), (82, 3), (82, 5), (84, 9), (84, 2), (84, 1), (84, 3), (84, 2), (84, 1), (84, 6), (84, 1), (85, 4), (86, 8), (87, 7), (87, 2), (87, 6), (88, 7), (89, 2), (90, 5), (90, 7), (90, 1), (91, 2), (91, 2), (91, 7), (91, 4), (91, 4), (91, 7), (92, 3), (92, 3), (93, 7), (93, 3), (93, 6), (93, 3), (94, 9), (95, 1), (95, 9), (96, 3), (96, 3), (97, 1), (97, 3), (97, 4),
                           (97, 9), (97, 9), (98, 8), (98, 4), (98, 3), (98, 8), (98, 8), (98, 8), (99, 8), (99, 8), (99, 6), (99, 3), (99, 5), (100, 9), (100, 1), (100, 6), (100, 7), (100, 8), (100, 6), (101, 4), (102, 8), (102, 8), (102, 1), (102, 8), (103, 5), (104, 4), (105, 9), (106, 6), (106, 3), (107, 3), (107, 9), (107, 3), (107, 8), (108, 9), (109, 8), (110, 6), (110, 7), (112, 5), (112, 9), (112, 5), (112, 4), (113, 5), (114, 5), (114, 6), (114, 3), (114, 7), (115, 1), (116, 3), (116, 8), (116, 9), (116, 7), (116, 2), (117, 6), (117, 1), (117, 8), (117, 9), (118, 8), (119, 9), (119, 5), (119, 1), (119, 6), (119, 2), (119, 4), (120, 4), (120, 4), (120, 1), (120, 4), (120, 5), (121, 5), (121, 5), (121, 9), (121, 5), (121, 9), (121, 9), (121, 1), (122, 2), (122, 5), (122, 2), (122, 9), (123, 9), (123, 9), (123, 5), (124, 4), (124, 1), (125, 8), (126, 5), (126, 9), (126, 3), (126, 6), (127, 4), (127, 3), (127, 8), (127, 7), (128, 5), (128, 1), (128, 1), (129, 7), (129, 4), (129, 9), (129, 7), (130, 9), (130, 2), (131, 5), (131, 1), (131, 7), (132, 3), (133, 9), (133, 2), (133, 3), (133, 9), (134, 7), (135, 2), (135, 7), (135, 6), (136, 9), (137, 9), (137, 6), (137, 4), (138, 4), (138, 7), (138, 7), (138, 4), (138, 4), (139, 2), (139, 2), (139, 8), (139, 7), (140, 7), (140, 4), (140, 2), (140, 6), (141, 7), (141, 6), (141, 5), (142, 9), (142, 6), (142, 4), (142, 4), (142, 8), (142, 9), (143, 2), (143, 8), (144, 1), (144, 3), (145, 3), (145, 9), (146, 8), (146, 7), (147, 4), (147, 4), (147, 9), (148, 7), (148, 3), (149, 6), (150, 6), (150, 2), (150, 6), (150, 9), (151, 3), (151, 8), (152, 8), (153, 6), (153, 5), (153, 9), (155, 3), (155, 4), (155, 2), (155, 5), (155, 4), (156, 2), (156, 8), (156, 5), (156, 7), (157, 6), (157, 3), (157, 3), (157, 7), (157, 2), (158, 7), (158, 2), (159, 5), (159, 3), (159, 7), (160, 1), (160, 2), (160, 7), (160, 1), (160, 6), (160, 1), (161, 6), (161, 1), (161, 3), (162, 9), (162, 6), (162, 4), (162, 3), (163, 5), (163, 9), (164, 6), (164, 1), (165, 2), (165, 2), (165, 3), (166, 4), (166, 3), (167, 1), (167, 2), (168, 8), (168, 3), (169, 5), (169, 7), (170, 1), (170, 3), (170, 4), (171, 8), (171, 1), (171, 7), (171, 9), (172, 7), (173, 4), (173, 4), (173, 4), (174, 7), (174, 2), (175, 7), (176, 1), (176, 2), (176, 1), (176, 2), (176, 6), (177, 7), (177, 8), (177, 2), (177, 5), (177, 7), (177, 3), (178, 4), (179, 5), (179, 3), (181, 7), (181, 6), (181, 8), (181, 6), (182, 2), (182, 6), (183, 1), (183, 7), (184, 4), (184, 1), (184, 3), (185, 8), (185, 4), (185, 5), (186, 6), (186, 1), (186, 2), (186, 5), (188, 9), (188, 1), (188, 2), (189, 4), (189, 5), (189, 7), (189, 4), (190, 7), (190, 3), (191, 8), (191, 9), (191, 6), (192, 4), (192, 4), (193, 8), (193, 9), (193, 5), (194, 1), (194, 2), (194, 4), (195, 3), (195, 3), (195, 3), (196, 1), (196, 7), (197, 5), (197, 7), (197, 2), (197, 1), (199, 8), (199, 3), (200, 5), (201, 1), (201, 2), (201, 2), (201, 5), (201, 2), (202, 8), (202, 5), (202, 5), (202, 6), (202, 6), (202, 2), (203, 3), (203, 9), (203, 3), (203, 7), (204, 2), (204, 7), (205, 3), (205, 9), (205, 8), (205, 2), (206, 8), (206, 8), (207, 5), (208, 7), (209, 2), (209, 1), (209, 6), (210, 9), (211, 6), (212, 2), (214, 8), (214, 3), (214, 2), (215, 8), (216, 4), (216, 7), (217, 8), (218, 2), (218, 6), (219, 7), (220, 8), (222, 7), (222, 2), (223, 1), (223, 1), (223, 1), (223, 3), (224, 2), (224, 7), (224, 5), (225, 6), (225, 1), (225, 8), (226, 4), (227, 3), (228, 3), (228, 1), (228, 3), (230, 3), (230, 1), (230, 2), (230, 5), (231, 3), (231, 3), (231, 4), (231, 1), (231, 9), (232, 5), (232, 8), (233, 7), (233, 2), (233, 1), (233, 2), (234, 5), (235, 5), (235, 7), (236, 8), (236, 1), (237, 3), (238, 8), (238, 5), (238, 3), (238, 5), (238, 1), (238, 4), (239, 4), (239, 1), (240, 9), (245, 8)]

D10_SEISCENTOS_ELEMENTOS = [(0, 10)] + D9_SEISCENTOS_ELEMENTOS[1:]

D9_MIL_ELEMENTOS = [(0, 5), (1, 6), (4, 9), (7, 7), (8, 4), (8, 5), (8, 7), (9, 9), (9, 5), (10, 9), (10, 9), (10, 3), (10, 2), (10, 7), (10, 8), (10, 5), (11, 4), (11, 1), (11, 3), (11, 7), (11, 1), (11, 8), (12, 4), (12, 3), (12, 8), (12, 4), (13, 9), (13, 1), (13, 9), (13, 2), (13, 6), (13,
                                                                                                                                                                                                                                                                                                   9), (14, 1), (14, 4), (16, 9), (16, 3), (16, 1), (16, 7), (17, 4), (17, 8), (17, 5), (17, 1), (18, 9), (18, 8), (18, 5), (18, 8), (18, 2), (18, 3), (18, 8), (18, 8), (19, 6), (19, 5), (19, 9), (19, 2), (19, 7), (20, 2), (20, 5), (20, 6), (22, 1), (22, 5), (22, 1), (22, 3), (22, 3), (22, 7), (23, 9), (23, 3), (24, 5), (24, 9), (24, 3), (24, 9), (24, 3), (25, 5), (25, 1), (25, 7), (25, 8), (26, 3), (27, 3), (27, 3), (27, 4), (27, 7), (27, 5), (27, 9), (28, 9), (29, 4), (29, 5), (29, 6), (29, 3), (29, 1), (29, 2), (30, 6), (30, 5), (31, 8), (31, 6), (31, 9), (31, 8), (31, 1), (31, 6), (32, 2), (32, 4), (32, 1), (32, 5), (32, 4), (33, 3), (33, 9), (33, 9), (33, 4), (33, 7), (33, 9), (33, 6), (33, 6), (33, 1), (34, 6), (34, 1), (34, 7), (34, 2), (34, 6), (34, 6), (34, 8), (34, 6), (35, 5), (35, 2), (35, 5), (36, 8), (37, 8), (37, 9), (38, 9), (38, 3), (38, 7), (39, 2), (39, 5), (39, 9), (39, 7), (40, 6), (40, 2), (40, 2), (41, 1), (41, 3), (41, 2), (41, 1), (41, 8),
                    (41, 9), (41, 5), (42, 1), (42, 5), (43, 4), (43, 1), (43, 6), (43, 9), (43, 4), (43, 9), (43, 6), (43, 6), (43, 4), (44, 2), (44, 9), (44, 9), (44, 7), (44, 1), (45, 2), (45, 3), (45, 9), (45, 5), (45, 7), (45, 3), (46, 8), (46, 5), (47, 4), (47, 8), (47, 3), (47, 7), (47, 6), (47, 7), (47, 1), (47, 3), (48, 8), (48, 7), (48, 5), (49, 7), (49, 7), (49, 2), (49, 8), (50, 8), (50, 1), (50, 5), (50, 1), (51, 4), (51, 3), (51, 7), (52, 7), (52, 9), (52, 9), (52, 7), (53, 3), (53, 9), (53, 5), (53, 6), (53, 1), (54, 3), (54, 1), (54, 4), (54, 6), (55, 7), (55, 4), (55, 2), (56, 4), (56, 9), (56, 5), (56, 3), (56, 8), (56, 9), (57, 5), (57, 1), (57, 1), (57, 5), (57, 1), (57, 7), (57, 2), (58, 8), (58, 9), (58, 2), (58, 4), (58, 5), (58, 1), (58, 5), (58, 4), (59, 8), (60, 1), (60, 8), (60, 2), (60, 5), (60, 4), (60, 3), (60, 8), (61, 2), (61, 7), (61, 5), (61, 5), (61, 3), (62, 9), (62, 7), (62, 2), (62, 9), (63, 6), (63, 6), (63, 7), (64, 4), (64, 4), (64, 2), (64, 1), (64, 1), (64, 3), (64, 4), (65, 2), (65, 3), (65, 8), (65, 8), (65, 1), (66, 8), (66, 6), (66, 1), (67, 3), (67, 2), (67, 7), (67, 8), (67, 6), (67, 9), (68, 1), (68, 3), (69, 2), (70, 6), (70, 7), (70, 3), (70, 1), (70, 2), (71, 8), (71,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    7), (71, 3), (71, 1), (71, 8), (71, 3), (72, 4), (72, 2), (72, 4), (73, 1), (73, 5), (73, 1), (73, 4), (74, 1), (74, 4), (74, 8), (74, 3), (75, 3), (75, 2), (75, 9), (76, 8), (76, 1), (76, 8), (76, 1), (76, 1), (76, 7), (76, 9), (77, 5), (77, 5), (78, 3), (78, 2), (78, 6), (78, 5), (78, 1), (78, 3), (78, 4), (79, 5), (79, 4), (79, 3), (79, 6), (80, 9), (80, 7), (80, 5), (80, 6), (81, 6), (81, 1), (81, 1), (81, 6), (81, 7), (82, 2), (82, 5), (82, 1), (83, 6), (83, 4), (83, 2), (83, 7), (83, 2), (83, 4), (83, 8), (83, 8), (83, 7), (83, 7), (84, 1), (84, 4), (84, 3), (84, 1), (84, 3), (84, 4), (85, 1), (85, 7), (85, 3), (85, 1), (86, 3), (86, 6), (86, 7), (87, 4), (87, 9), (87, 6), (88, 3), (88, 7), (88, 3), (88, 8), (88, 9), (88, 6), (89, 3), (89, 1), (89, 5), (89, 6), (89, 5), (89, 9), (89, 3), (90, 8), (90, 9), (90, 1), (90, 7), (91, 2), (91, 3), (91, 4), (91, 3), (91, 6), (92, 9), (92, 5), (92, 5), (92, 9), (92, 5), (94, 9), (94, 3), (94, 8), (94, 1), (94, 9),
                    (94, 4), (95, 2), (95, 3), (95, 9), (95, 4), (95, 2), (96, 6), (96, 8), (96, 2), (96, 4), (96, 7), (96, 8), (97, 1), (97, 5), (97, 6), (98, 9), (98, 6), (98, 5), (99, 7), (99, 1), (99, 2), (99, 3), (99, 5), (99, 2), (100, 9), (100, 1), (100, 8), (100, 1), (100, 9), (101, 5), (101, 1), (101, 2), (101, 9), (102, 5), (102, 4), (102, 9), (103, 3), (103, 2), (103, 4), (103, 4), (103, 8), (104, 8), (104, 7), (104, 6), (105, 6), (105, 7), (106, 2), (106, 3), (106, 2), (106, 2), (106, 4), (106, 8), (106, 6), (106, 2), (107, 6), (107, 5), (107, 3), (108, 3), (108, 5), (108, 6), (108, 1), (108, 6), (108, 4), (109, 4), (109, 4), (110, 6), (110, 4), (110, 5), (110, 3), (110, 7), (110, 2), (111, 2), (111, 8), (111, 5), (112, 7), (112,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           5), (112, 6), (112, 5), (113, 8), (113, 5), (114, 1), (114, 9), (114, 6), (114, 5), (114, 3), (115, 8), (115, 2), (115, 7), (115, 5), (116, 4), (116, 9), (116, 7), (116, 1), (116, 6), (117, 6), (117, 6), (117, 6), (118, 2), (118, 9), (119, 8),
                    (119, 6), (120, 6), (120, 1), (120, 5), (120, 7), (121, 1), (121, 2), (121, 9), (122, 5), (122, 1), (122, 9), (122, 7), (124, 8), (124, 9), (124, 8), (124, 4), (125, 3), (125, 5), (126, 9), (127, 3), (127, 2), (127, 7), (127, 5), (127, 3), (128, 6), (128, 8), (128, 5), (128, 4), (129, 8), (129, 1), (130, 2), (130, 4), (130, 6), (130, 9), (130, 7), (130, 1), (130, 4), (130, 2), (131, 1), (131, 8), (131, 4), (131, 4), (132, 9), (132, 3), (132, 6), (132, 4), (132, 2), (132, 4), (133, 6), (133, 8), (134, 9), (134, 2), (135, 2), (135, 3), (135, 9), (135, 6), (135, 8), (135, 2), (136, 3), (136, 9), (136, 5), (136, 1), (136, 7), (136, 2), (136, 6), (137, 8), (137, 6), (137, 8), (137, 9), (138, 1), (138, 9), (138, 6), (138, 4), (138, 4), (138, 1), (138, 2), (139, 8), (139, 9), (139, 9), (139, 2), (139, 5), (140, 2), (140, 9), (140, 4), (141, 7), (142, 9), (142, 1), (142, 6), (142, 7), (142, 8), (142, 1), (142, 5), (142, 2), (143, 4), (143, 2), (143, 1), (143, 3), (143,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               6), (144, 8), (145, 7), (145, 6), (145, 3), (145, 4), (146, 8), (146, 3), (146, 8), (146, 5), (146, 9), (146, 1), (146, 4), (146, 4), (146, 9), (147, 1), (147, 6), (147, 4), (147, 4), (148, 6), (148, 6), (148, 2), (149, 9), (149, 8), (149, 7),
                    (149, 8), (149, 5), (149, 6), (150, 9), (150, 9), (150, 4), (151, 9), (151, 8), (152, 2), (152, 9), (152, 3), (152, 5), (152, 1), (152, 5), (153, 1), (153, 1), (153, 9), (153, 1), (154, 7), (154, 1), (154, 5), (154, 5), (154, 7), (154, 9), (154, 6), (155, 4), (155, 7), (155, 2), (156, 7), (156, 6), (156, 1), (157, 9), (157, 5), (157, 9), (157, 7), (157, 9), (157, 1), (157, 8), (158, 7), (158, 2), (158, 4), (158, 6), (158, 7), (159, 6), (159, 4), (159, 7), (159, 6), (159, 3), (159, 4), (159, 7), (160, 4), (160, 4), (161, 2), (161, 2), (161, 3), (162, 7), (162, 4), (162, 8), (163, 9), (163, 6), (163, 1), (163, 7), (163, 9), (163, 2), (164, 6), (164, 8), (164, 4), (164, 3), (164, 1), (165, 8), (165, 5), (165, 3), (165, 6), (165, 3), (167, 4), (167, 2), (167, 2), (168, 2), (168, 1), (168, 5), (168, 8), (168, 8), (169, 3), (169, 1), (169, 2), (169, 3), (169, 6), (171, 8), (171, 5), (171, 2), (172, 3), (172, 5), (172, 8), (172, 9), (172, 5), (172, 5), (173, 8), (173,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               8), (173, 3), (173, 2), (173, 9), (173, 5), (173, 4), (174, 7), (174, 1), (174, 9), (174, 7), (174, 1), (174, 2), (174, 1), (175, 4), (175, 7), (175, 2), (175, 6), (176, 1), (176, 4), (176, 1), (176, 8), (177, 3), (177, 9), (177, 5), (177, 3),
                    (177, 7), (177, 3), (178, 5), (178, 3), (179, 5), (179, 6), (179, 8), (179, 9), (179, 8), (180, 8), (180, 7), (180, 7), (181, 8), (181, 5), (182, 2), (182, 9), (182, 2), (182, 3), (183, 4), (183, 4), (183, 9), (183, 2), (183, 4), (183, 8), (183, 6), (184, 8), (184, 8), (184, 3), (185, 2), (185, 1), (185, 3), (186, 5), (186, 6), (186, 7), (186, 5), (186, 1), (187, 5), (188, 5), (188, 3), (188, 8), (189, 3), (189, 4), (189, 1), (189, 6), (189, 9), (189, 5), (189, 7), (190, 6), (190, 3), (190, 3), (190, 7), (190, 3), (190, 3), (190, 5), (191, 9), (191, 3), (191, 3), (191, 3), (192, 8), (192, 9), (192, 1), (192, 5), (192, 9), (193, 8), (193, 5), (193, 7), (193, 6), (193, 4), (193, 3), (194, 5), (194, 5), (194, 7), (194, 3), (194, 1), (194, 2), (194, 9), (195, 1), (195, 9), (195, 3), (195, 6), (196, 9), (196, 8), (196, 6), (196, 6), (196, 1), (196, 7), (196, 8), (197, 1), (197, 1), (197, 5), (198, 4), (198, 1), (198, 9), (198, 3), (198, 9), (199, 7), (199, 6), (199,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               8), (199, 6), (200, 2), (201, 6), (201, 1), (201, 1), (201, 5), (201, 5), (202, 6), (202, 5), (202, 6), (202, 1), (202, 3), (202, 6), (202, 6), (203, 6), (203, 9), (204, 7), (204, 9), (204, 3), (204, 4), (204, 2), (204, 3), (205, 3), (205, 5),
                    (205, 4), (205, 5), (206, 3), (206, 3), (206, 8), (206, 8), (207, 8), (207, 5), (207, 7), (207, 3), (208, 8), (208, 6), (208, 2), (208, 1), (208, 5), (209, 4), (209, 3), (209, 2), (209, 3), (210, 1), (210, 7), (210, 2), (210, 2), (210, 9), (210, 4), (211, 3), (211, 9), (211, 1), (211, 7), (211, 8), (212, 5), (212, 6), (212, 3), (213, 5), (213, 8), (213, 8), (213, 2), (214, 9), (214, 4), (214, 3), (214, 6), (214, 3), (215, 8), (215, 2), (216, 8), (216, 8), (216, 3), (216, 4), (217, 1), (217, 9), (217, 8), (217, 1), (217, 7), (217, 8), (217, 6), (218, 2), (218, 8), (218, 4), (218, 6), (218, 4), (219, 9), (219, 7), (219, 4), (220, 1), (220, 1), (220, 5), (220, 8), (220, 9), (220, 1), (220, 1), (221, 6), (221, 7), (222, 6), (222, 3), (222, 7), (223, 8), (223, 3), (223, 1), (223, 6), (224, 8), (224, 4), (224, 2), (224, 1), (224, 7), (224, 3), (225, 3), (225, 6), (225, 9), (225, 1), (225, 1), (225, 1), (225, 8), (225, 7), (226, 1), (227, 2), (227, 6), (227, 3), (228,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               7), (228, 8), (228, 1), (228, 4), (228, 2), (229, 8), (229, 7), (229, 8), (229, 2), (230, 3), (230, 7), (230, 1), (230, 9), (230, 3), (230, 6), (231, 5), (231, 3), (232, 4), (232, 6), (232, 3), (232, 1), (233, 1), (233, 6), (233, 8), (234, 2),
                    (234, 1), (235, 8), (236, 5), (236, 7), (236, 8), (236, 2), (236, 4), (236, 2), (236, 2), (236, 9), (237, 5), (237, 7), (237, 1), (238, 3), (238, 8), (238, 3), (239, 3), (239, 6), (239, 8), (239, 6), (239, 5), (240, 6), (240, 5), (240, 5), (240, 8), (240, 9), (240, 1), (245, 8)]

D10_MIL_ELEMENTOS = [(0, 10)] + D9_MIL_ELEMENTOS[1:]

T0_SEISCENTOS_ELEMENTOS = [(0, 10), (0, 5), (0, 1), (0, 8), (0, 1), (0, 5), (0, 4), (0, 6), (0, 8), (0, 1), (0, 7), (0, 7), (0, 5), (0, 3), (0, 9), (0, 1), (0, 8), (0, 7), (0, 1), (0, 7), (0, 1), (0, 6), (0, 9), (0, 3), (0, 1), (0, 7), (0, 4), (0, 6), (0, 2), (0, 5), (0, 3), (0, 3), (0, 1), (0, 3), (0, 6), (0, 1), (0, 6), (0, 8), (0, 4), (0, 9), (0, 4), (0, 2), (0, 3), (0, 3), (0, 7), (0, 9), (0, 4), (0, 1), (0, 8), (0, 8), (0, 3), (0, 6), (0, 1), (0, 5), (0, 2), (0, 1), (0, 7), (0, 4), (0, 5), (0, 5), (0, 7), (0, 8), (0, 7), (0, 3), (0, 9), (0, 8), (0, 6), (0, 7), (0, 3), (0, 5), (0, 7), (0, 7), (0, 3), (0, 3), (0, 4), (0, 4), (0, 5), (0, 4), (0, 9), (0, 1), (0, 6), (0, 6), (0, 2), (0, 5), (0, 8), (0, 7), (0, 1), (0, 3), (0, 6), (0, 3), (0, 2), (0, 5), (0, 4), (0, 7), (0, 3), (0, 8), (0, 5), (0, 1), (0, 7), (0, 2), (0, 1), (0, 7), (0, 1), (0, 3), (0, 5), (0, 9), (0, 5), (0, 5), (0, 2), (0, 5), (0, 6), (0, 3), (0, 8), (0, 1), (0, 1), (0, 6), (0, 7), (0, 3), (0, 6), (0, 3), (0, 6), (0, 4), (0, 7), (0, 4), (0, 5), (0, 8), (0, 3), (0, 5), (0, 4), (0, 4), (0, 8), (0, 8), (0, 8), (0, 3), (0, 7), (0, 4), (0, 8), (0, 7), (0, 4), (0, 1), (0, 3), (0, 7), (0, 2), (0, 8), (0, 5), (0, 3), (0, 3), (0, 4), (0, 5), (0, 4), (0, 7), (0, 3), (0, 2), (0, 2), (0, 3), (0, 5), (0, 7), (0, 6), (0, 5), (0, 1), (0, 1), (0, 3), (0, 8), (0, 5), (0, 2), (0, 6), (0, 4), (0, 8), (0, 3), (0, 7), (0, 5), (0, 9), (0, 1), (0, 8), (0, 4), (0, 7), (0, 8), (0, 9), (0, 8), (0, 9), (0, 2), (0, 6), (0, 6), (0, 8), (0, 7), (0, 9), (0, 1), (0, 4), (0, 7), (0, 1), (0, 6), (0, 5), (0, 3), (0, 5), (0, 9), (0, 3), (0, 8), (0, 3), (0, 3), (0, 4), (0, 5), (0, 2), (0, 9), (0, 6), (0, 1), (0, 6), (0, 6), (0, 5), (0, 3), (0, 7), (0, 8), (0, 2), (0, 3), (0, 9), (0, 2), (0, 6), (0, 7), (0, 4), (0, 7), (0, 1), (0, 6), (0, 7), (0, 9), (0, 8), (0, 1), (0, 7), (0, 6), (0, 4), (0, 5), (0, 5), (0, 2), (0, 4), (0, 3), (0, 9), (0, 6), (0, 2), (0, 8), (0, 3), (0, 2), (0, 7), (0, 8), (0, 2), (0, 1), (0, 9), (0, 2), (0, 6), (0, 4), (0, 1), (0, 1), (0, 9), (0, 3), (0, 6), (0, 2), (0, 8), (0, 7), (0, 8), (0, 1), (0, 6), (0, 6), (0, 7), (0, 6), (0, 9), (0, 1), (0, 5), (0, 5), (0, 8), (0, 5), (0, 7), (0, 1), (0, 8), (0, 8), (0, 7), (0, 7), (0, 6), (0, 1), (0, 7), (0, 7), (0, 9), (0, 8), (0, 9), (0, 3), (0, 3), (0, 4), (0, 3), (0, 3), (0, 9), (0, 1), (0, 1), (0, 4), (0, 2), (0, 3), (0, 1), (0, 9), (0, 5), (0, 1), (0, 4), (
    0, 4), (0, 9), (0, 5), (0, 7), (0, 2), (0, 8), (0, 3), (0, 4), (0, 8), (0, 4), (0, 9), (0, 5), (0, 7), (0, 2), (0, 4), (0, 8), (0, 2), (0, 9), (0, 8), (0, 3), (0, 2), (0, 9), (0, 2), (0, 5), (0, 5), (0, 8), (0, 9), (0, 7), (0, 1), (0, 5), (0, 3), (0, 3), (0, 7), (0, 2), (0, 4), (0, 4), (0, 5), (0, 6), (0, 8), (0, 2), (0, 4), (0, 9), (0, 5), (0, 8), (0, 1), (0, 2), (0, 5), (0, 2), (0, 1), (0, 6), (0, 5), (0, 7), (0, 2), (0, 4), (0, 3), (0, 5), (0, 8), (0, 5), (0, 6), (0, 4), (0, 9), (0, 7), (0, 7), (0, 1), (0, 9), (0, 6), (0, 9), (0, 2), (0, 5), (0, 2), (0, 9), (0, 7), (0, 9), (0, 2), (0, 7), (0, 7), (0, 4), (0, 4), (0, 2), (0, 8), (0, 2), (0, 3), (0, 3), (0, 4), (0, 6), (0, 3), (0, 2), (0, 9), (0, 4), (0, 9), (0, 9), (0, 6), (0, 6), (0, 9), (0, 2), (0, 3), (0, 3), (0, 8), (0, 3), (0, 3), (0, 7), (0, 8), (0, 3), (0, 3), (0, 2), (0, 8), (0, 6), (0, 2), (0, 6), (0, 2), (0, 8), (0, 2), (0, 6), (0, 3), (0, 1), (0, 3), (0, 3), (0, 4), (0, 6), (0, 4), (0, 7), (0, 9), (0, 6), (0, 5), (0, 8), (0, 8), (0, 5), (0, 6), (0, 3), (0, 4), (0, 4), (0, 9), (0, 7), (0, 4), (0, 8), (0, 3), (0, 7), (0, 9), (0, 5), (0, 3), (0, 5), (0, 7), (0, 2), (0, 4), (0, 6), (0, 8), (0, 5), (0, 8), (0, 4), (0, 3), (0, 2), (0, 6), (0, 1), (0, 4), (0, 9), (0, 7), (0, 4), (0, 1), (0, 3), (0, 6), (0, 3), (0, 5), (0, 7), (0, 6), (0, 8), (0, 5), (0, 2), (0, 2), (0, 6), (0, 6), (0, 8), (0, 3), (0, 4), (0, 5), (0, 7), (0, 1), (0, 4), (0, 8), (0, 2), (0, 4), (0, 1), (0, 7), (0, 1), (0, 8), (0, 3), (0, 8), (0, 6), (0, 2), (0, 3), (0, 4), (0, 3), (0, 2), (0, 4), (0, 5), (0, 1), (0, 6), (0, 3), (0, 9), (0, 7), (0, 9), (0, 8), (0, 1), (0, 5), (0, 4), (0, 2), (0, 3), (0, 3), (0, 7), (0, 2), (0, 4), (0, 6), (0, 3), (0, 3), (0, 2), (0, 1), (0, 1), (0, 7), (0, 3), (0, 2), (0, 9), (0, 9), (0, 9), (0, 6), (0, 7), (0, 4), (0, 1), (0, 4), (0, 6), (0, 1), (0, 9), (0, 9), (0, 6), (0, 8), (0, 4), (0, 8), (0, 4), (0, 1), (0, 2), (0, 9), (0, 5), (0, 5), (0, 7), (0, 1), (0, 8), (0, 9), (0, 1), (0, 1), (0, 5), (0, 1), (0, 8), (0, 3), (0, 3), (0, 3), (0, 6), (0, 8), (0, 3), (0, 3), (0, 2), (0, 1), (0, 1), (0, 2), (0, 9), (0, 2), (0, 5), (0, 5), (0, 4), (0, 9), (0, 4), (0, 3), (0, 3), (0, 2), (0, 4), (0, 8), (0, 8), (0, 4), (0, 5), (0, 3), (0, 2), (0, 4), (0, 7), (0, 3), (0, 9), (0, 9), (0, 2), (0, 1), (0, 5), (0, 1), (0, 4), (0, 9), (0, 6), (0, 4), (0, 7), (0, 9), (0, 5), (0, 9), (0, 3), (0, 5), (0, 5), (0, 7)]

T0_MIL_ELEMENTOS = [(0, 4), (0, 5), (0, 4), (0, 1), (0, 5), (0, 2), (0, 6), (0, 9), (0, 2), (0, 1), (0, 5), (0, 9), (0, 5), (0, 4), (0, 5), (0, 3), (0, 9), (0, 5), (0, 2), (0, 7), (0, 3), (0, 5), (0, 6), (0, 2), (0, 9), (0, 6), (0, 6), (0, 4), (0, 9), (0, 4), (0, 8), (0, 4), (0, 1), (0, 1), (0, 6), (0, 5), (0, 3), (0, 2), (0, 8), (0, 6), (0, 1), (0, 2), (0, 2), (0, 9), (0, 4), (0, 5), (0, 8), (0, 4), (0, 9), (0, 3), (0, 6), (0, 6), (0, 5), (0, 2), (0, 8), (0, 7), (0, 5), (0, 6), (0, 7), (0, 5), (0, 7), (0, 5), (0, 4), (0, 3), (0, 8), (0, 7), (0, 6), (0, 2), (0, 2), (0, 8), (0, 7), (0, 5), (0, 6), (0, 8), (0, 3), (0, 4), (0, 1), (0, 2), (0, 4), (0, 1), (0, 7), (0, 9), (0, 8), (0, 9), (0, 2), (0, 5), (0, 4), (0, 2), (0, 4), (0, 8), (0, 3), (0, 1), (0, 9), (0, 9), (0, 1), (0, 9), (0, 7), (0, 8), (0, 9), (0, 2), (0, 8), (0, 4), (0, 1), (0, 3), (0, 4), (0, 6), (0, 4), (0, 4), (0, 8), (0, 6), (0, 9), (0, 6), (0, 6), (0, 8), (0, 7), (0, 4), (0, 8), (0, 3), (0, 9), (0, 2), (0, 6), (0, 7), (0, 6), (0, 4), (0, 6), (0, 4), (0, 7), (0, 1), (0, 4), (0, 9), (0, 2), (0, 9), (0, 9), (0, 2), (0, 2), (0, 8), (0, 9), (0, 3), (0, 9), (0, 5), (0, 7), (0, 8), (0, 7), (0, 1), (0, 4), (0, 7), (0, 7), (0, 8), (0, 1), (0, 8), (0, 4), (0, 5), (0, 4), (0, 8), (0, 6), (0, 5), (0, 1), (0, 4), (0, 8), (0, 8), (0, 9), (0, 4), (0, 4), (0, 2), (0, 8), (0, 9), (0, 2), (0, 7), (0, 8), (0, 6), (0, 5), (0, 5), (0, 6), (0, 2), (0, 3), (0, 5), (0, 6), (0, 3), (0, 6), (0, 4), (0, 2), (0, 9), (0, 2), (0, 6), (0, 8), (0, 7), (0, 5), (0, 3), (0, 5), (0, 8), (0, 8), (0, 2), (0, 7), (0, 8), (0, 6), (0, 4), (0, 5), (0, 5), (0, 7), (0, 6), (0, 8), (0, 3), (0, 5), (0, 7), (0, 9), (0, 1), (0, 6), (0, 2), (0, 1), (0, 6), (0, 2), (0, 2), (0, 8), (0, 2), (0, 9), (0, 4), (0, 8), (0, 8), (0, 6), (0, 2), (0, 8), (0, 5), (0, 7), (0, 4), (0, 4), (0, 7), (0, 5), (0, 4), (0, 7), (0, 6), (0, 7), (0, 4), (0, 1), (0, 4), (0, 7), (0, 9), (0, 4), (0, 6), (0, 3), (0, 6), (0, 1), (0, 4), (0, 4), (0, 3), (0, 9), (0, 1), (0, 3), (0, 1), (0, 5), (0, 2), (0, 1), (0, 7), (0, 7), (0, 8), (0, 7), (0, 6), (0, 7), (0, 3), (0, 1), (0, 8), (0, 4), (0, 9), (0, 7), (0, 8), (0, 1), (0, 2), (0, 4), (0, 5), (0, 4), (0, 4), (0, 7), (0, 6), (0, 4), (0, 5), (0, 6), (0, 5), (0, 5), (0, 6), (0, 3), (0, 4), (0, 7), (0, 5), (0, 3), (0, 9), (0, 5), (0, 6), (0, 3), (0, 7), (0, 9), (0, 6), (0, 4), (0, 2), (0, 6), (0, 7), (0, 3), (0, 5), (0, 3), (0, 6), (0, 7), (0, 6), (0, 2), (0, 1), (0, 4), (0, 5), (0, 5), (0, 1), (0, 1), (0, 3), (0, 5), (0, 2), (0, 2), (0, 8), (0, 3), (0, 7), (0, 9), (0, 3), (0, 1), (0, 2), (0, 5), (0, 9), (0, 7), (0, 1), (0, 4), (0, 7), (0, 3), (0, 9), (0, 3), (0, 9), (0, 9), (0, 9), (0, 6), (0, 9), (0, 1), (0, 6), (0, 9), (0, 4), (0, 4), (0, 6), (0, 6), (0, 5), (0, 3), (0, 9), (0, 1), (0, 1), (0, 8), (0, 5), (0, 6), (0, 8), (0, 5), (0, 2), (0, 3), (0, 6), (0, 8), (0, 4), (0, 1), (0, 4), (0, 4), (0, 8), (0, 5), (0, 6), (0, 8), (0, 6), (0, 8), (0, 2), (0, 8), (0, 9), (0, 5), (0, 5), (0, 3), (0, 4), (0, 8), (0, 7), (0, 6), (0, 6), (0, 1), (0, 2), (0, 3), (0, 4), (0, 9), (0, 6), (0, 4), (0, 3), (0, 4), (0, 8), (0, 2), (0, 6), (0, 2), (0, 3), (0, 9), (0, 8), (0, 4), (0, 8), (0, 5), (0, 8), (0, 4), (0, 9), (0, 2), (0, 8), (0, 6), (0, 6), (0, 2), (0, 5), (0, 5), (0, 8), (0, 2), (0, 4), (0, 1), (0, 8), (0, 2), (0, 5), (0, 7), (0, 6), (0, 3), (0, 3), (0, 3), (0, 4), (0, 5), (0, 6), (0, 2), (0, 6), (0, 7), (0, 1), (0, 3), (0, 6), (0, 7), (0, 8), (0, 8), (0, 2), (0, 7), (0, 5), (0, 7), (0, 2), (0, 9), (0, 7), (0, 1), (0, 7), (0, 1), (0, 5), (0, 3), (0, 3), (0, 1), (0, 4), (0, 3), (0, 7), (0, 5), (0, 3), (0, 7), (0, 9), (0, 1), (0, 1), (0, 5), (0, 5), (0, 7), (0, 3), (0, 8), (0, 9), (0, 2), (0, 5), (0, 7), (0, 3), (0, 3), (0, 3), (0, 5), (0, 5), (0, 6), (0, 9), (0, 1), (0, 8), (0, 2), (0, 3), (0, 3), (0, 4), (0, 2), (0, 4), (0, 9), (0, 1), (0, 9), (0, 4), (0, 3), (0, 4), (0, 5), (0, 8), (0, 2), (0, 4), (0, 6), (0, 8), (0, 2), (0, 7), (0, 6), (0, 2), (0, 5), (0, 1), (0, 2), (0, 4), (0, 1), (0, 8), (
    0, 4), (0, 8), (0, 3), (0, 1), (0, 8), (0, 5), (0, 4), (0, 5), (0, 7), (0, 2), (0, 7), (0, 1), (0, 4), (0, 7), (0, 6), (0, 2), (0, 6), (0, 4), (0, 2), (0, 5), (0, 2), (0, 9), (0, 2), (0, 2), (0, 4), (0, 4), (0, 5), (0, 3), (0, 7), (0, 9), (0, 5), (0, 8), (0, 2), (0, 2), (0, 9), (0, 2), (0, 5), (0, 6), (0, 5), (0, 7), (0, 8), (0, 9), (0, 6), (0, 3), (0, 3), (0, 2), (0, 5), (0, 2), (0, 8), (0, 2), (0, 3), (0, 5), (0, 3), (0, 8), (0, 2), (0, 1), (0, 8), (0, 8), (0, 9), (0, 2), (0, 2), (0, 6), (0, 9), (0, 6), (0, 8), (0, 8), (0, 9), (0, 5), (0, 3), (0, 2), (0, 6), (0, 9), (0, 2), (0, 4), (0, 6), (0, 8), (0, 1), (0, 5), (0, 7), (0, 2), (0, 7), (0, 5), (0, 6), (0, 6), (0, 8), (0, 3), (0, 5), (0, 5), (0, 1), (0, 9), (0, 1), (0, 4), (0, 1), (0, 3), (0, 1), (0, 2), (0, 6), (0, 9), (0, 2), (0, 4), (0, 1), (0, 6), (0, 8), (0, 9), (0, 6), (0, 7), (0, 5), (0, 9), (0, 6), (0, 4), (0, 9), (0, 3), (0, 2), (0, 8), (0, 8), (0, 5), (0, 3), (0, 2), (0, 7), (0, 9), (0, 5), (0, 5), (0, 7), (0, 2), (0, 2), (0, 4), (0, 6), (0, 3), (0, 3), (0, 1), (0, 2), (0, 8), (0, 7), (0, 7), (0, 8), (0, 1), (0, 1), (0, 9), (0, 5), (0, 4), (0, 8), (0, 3), (0, 1), (0, 6), (0, 7), (0, 2), (0, 4), (0, 4), (0, 1), (0, 3), (0, 2), (0, 3), (0, 6), (0, 4), (0, 8), (0, 3), (0, 9), (0, 7), (0, 4), (0, 8), (0, 6), (0, 3), (0, 4), (0, 3), (0, 9), (0, 6), (0, 8), (0, 5), (0, 8), (0, 8), (0, 4), (0, 1), (0, 2), (0, 1), (0, 1), (0, 5), (0, 7), (0, 3), (0, 2), (0, 6), (0, 8), (0, 3), (0, 3), (0, 8), (0, 8), (0, 4), (0, 5), (0, 4), (0, 6), (0, 7), (0, 6), (0, 4), (0, 3), (0, 2), (0, 3), (0, 5), (0, 2), (0, 6), (0, 2), (0, 8), (0, 2), (0, 3), (0, 3), (0, 3), (0, 6), (0, 8), (0, 8), (0, 1), (0, 2), (0, 9), (0, 6), (0, 1), (0, 6), (0, 7), (0, 4), (0, 7), (0, 4), (0, 1), (0, 9), (0, 6), (0, 6), (0, 2), (0, 1), (0, 6), (0, 9), (0, 3), (0, 8), (0, 7), (0, 4), (0, 1), (0, 9), (0, 5), (0, 6), (0, 7), (0, 9), (0, 7), (0, 1), (0, 4), (0, 7), (0, 7), (0, 4), (0, 2), (0, 7), (0, 9), (0, 5), (0, 5), (0, 6), (0, 7), (0, 4), (0, 2), (0, 7), (0, 1), (0, 5), (0, 3), (0, 1), (0, 6), (0, 1), (0, 1), (0, 4), (0, 9), (0, 9), (0, 4), (0, 6), (0, 6), (0, 9), (0, 1), (0, 5), (0, 7), (0, 1), (0, 6), (0, 5), (0, 8), (0, 8), (0, 5), (0, 8), (0, 1), (0, 4), (0, 1), (0, 7), (0, 8), (0, 6), (0, 9), (0, 7), (0, 4), (0, 9), (0, 4), (0, 7), (0, 9), (0, 6), (0, 5), (0, 2), (0, 7), (0, 3), (0, 6), (0, 8), (0, 2), (0, 8), (0, 9), (0, 8), (0, 8), (0, 4), (0, 1), (0, 3), (0, 4), (0, 1), (0, 5), (0, 9), (0, 4), (0, 5), (0, 2), (0, 4), (0, 8), (0, 4), (0, 1), (0, 9), (0, 1), (0, 4), (0, 9), (0, 7), (0, 2), (0, 8), (0, 1), (0, 8), (0, 7), (0, 8), (0, 8), (0, 1), (0, 6), (0, 8), (0, 4), (0, 3), (0, 8), (0, 7), (0, 2), (0, 8), (0, 8), (0, 3), (0, 3), (0, 8), (0, 7), (0, 7), (0, 3), (0, 3), (0, 3), (0, 8), (0, 4), (0, 4), (0, 7), (0, 8), (0, 4), (0, 1), (0, 1), (0, 6), (0, 1), (0, 3), (0, 8), (0, 4), (0, 7), (0, 5), (0, 2), (0, 6), (0, 4), (0, 3), (0, 8), (0, 5), (0, 2), (0, 7), (0, 8), (0, 9), (0, 7), (0, 4), (0, 5), (0, 4), (0, 6), (0, 7), (0, 1), (0, 2), (0, 6), (0, 7), (0, 7), (0, 6), (0, 5), (0, 4), (0, 5), (0, 3), (0, 3), (0, 2), (0, 8), (0, 3), (0, 7), (0, 7), (0, 4), (0, 3), (0, 4), (0, 4), (0, 5), (0, 4), (0, 1), (0, 2), (0, 1), (0, 2), (0, 6), (0, 8), (0, 2), (0, 4), (0, 4), (0, 5), (0, 3), (0, 3), (0, 9), (0, 3), (0, 6), (0, 8), (0, 7), (0, 4), (0, 5), (0, 8), (0, 7), (0, 9), (0, 5), (0, 6), (0, 8), (0, 3), (0, 8), (0, 7), (0, 5), (0, 1), (0, 1), (0, 7), (0, 5), (0, 6), (0, 6), (0, 3), (0, 6), (0, 5), (0, 7), (0, 4), (0, 5), (0, 1), (0, 5), (0, 2), (0, 3), (0, 5), (0, 9), (0, 6), (0, 8), (0, 7), (0, 9), (0, 9), (0, 3), (0, 1), (0, 1), (0, 7), (0, 3), (0, 2), (0, 4), (0, 4), (0, 1), (0, 9), (0, 7), (0, 6), (0, 1), (0, 8), (0, 2), (0, 6), (0, 2), (0, 1), (0, 7), (0, 9), (0, 3), (0, 1), (0, 9), (0, 4), (0, 7), (0, 6), (0, 5), (0, 7), (0, 7), (0, 1), (0, 5), (0, 1), (0, 6), (0, 5), (0, 7), (0, 4), (0, 9), (0, 6), (0, 7), (0, 7), (0, 2), (0, 5), (0, 6), (0, 5), (0, 8), (0, 8), (0, 9), (0, 7), (0, 8), (0, 4)]


@pytest.mark.parametrize(
    "input, expected_result",
    [
        ([1, D9_CEM_ELEMENTOS], 89),
        ([3, D9_CEM_ELEMENTOS], 0),
        ([7, D9_CEM_ELEMENTOS], 0),
        ([10, D9_CEM_ELEMENTOS], 0),
        ([3, [(0, 10)]], 0),
        ([5, D9_CEM_ELEMENTOS], 0),
        ([7, D9_CEM_ELEMENTOS], 0),
        ([9, D9_CEM_ELEMENTOS], 0),
        ([2, [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5),
                    (0, 6), (0, 7), (0, 8), (0, 9), (0, 10)]], 0),
        ([2, [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6),
                    (100, 7), (200, 8), (250, 9), (300, 10)]], 0),
        ([1, [(0, 1), (0, 2), (0, 3)]], 0),
        ([1, [(0, 1), (0, 2), (0, 10)]], 0),
    ],
)

def test_invalid(input, expected_result):
    actual = banco(*input)
    assert actual == expected_result
