-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: durva
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `quiz_que`
--

DROP TABLE IF EXISTS `quiz_que`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quiz_que` (
  `id` int NOT NULL AUTO_INCREMENT,
  `question` text NOT NULL,
  `option1` text NOT NULL,
  `option2` text NOT NULL,
  `option3` text NOT NULL,
  `option4` text NOT NULL,
  `correct_option` int NOT NULL,
  `code` varchar(10) NOT NULL,
  `qno` int NOT NULL,
  `organization` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=86 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quiz_que`
--

LOCK TABLES `quiz_que` WRITE;
/*!40000 ALTER TABLE `quiz_que` DISABLE KEYS */;
INSERT INTO `quiz_que` VALUES (1,'test','1','2','3','4',4,'333333',1,NULL),(7,'hello','fege','grr','htjy','jyj',4,'502201',1,NULL),(8,'grhr','geg','rhr','rhr','hr',2,'502201',2,NULL),(9,'ht','ee','hrg','ht','tt',2,'502201',3,NULL),(20,'hegb','rff','gtt','hyy','jjj',1,'270398',1,NULL),(21,'rf','frf','gyh','uju','yh',4,'270398',2,NULL),(22,'gtg','tgg','gtt','h','h',3,'270398',3,NULL),(38,'eeee','','','eeeee','',3,'556594',1,NULL),(39,'eeeee','','','eeee','',3,'556594',2,NULL),(40,'g','','','g','',3,'880093',1,NULL),(41,'g','','','g','',3,'880093',2,NULL),(42,'','','','','',1,'880093',3,NULL),(43,'hhhhh','','uuu','yyyy','',3,'722426',1,NULL),(44,'yy','','','yyyyyyyyy','',1,'722426',2,NULL),(45,'t','','tt','','',2,'609778',1,NULL),(46,'tt','','','tt','',3,'609778',2,NULL),(52,'Who is the father of C language?','Steve Jobs','James Gosling','Dennis Ritchie','Rasmus Lerdorf',3,'962079',1,NULL),(53,'All keywords in C are in?','LowerCase letters','UpperCase letters','CamelCase letters','nan',1,'962079',2,NULL),(54,'What is an example of iteration in C?','for','while','do-while','all',4,'962079',3,NULL),(55,'We cannot use the keyword ‘break’ simply within?','while','for','if-else','do-while',3,'962079',4,NULL),(56,'The global variables are ?','External','Internal','Both External and Internal','nan',1,'962079',5,NULL),(57,'Who is the father of C language?','Steve Jobs','James Gosling','Dennis Ritchie','Rasmus Lerdorf',3,'219344',1,NULL),(58,'All keywords in C are in?','LowerCase letters','UpperCase letters','CamelCase letters','nan',1,'219344',2,NULL),(59,'What is an example of iteration in C?','for','while','do-while','all',4,'219344',3,NULL),(60,'We cannot use the keyword ‘break’ simply within?','while','for','if-else','do-while',3,'219344',4,NULL),(61,'The global variables are ?','External','Internal','Both External and Internal','nan',1,'219344',5,NULL),(62,'xx','','x','','',2,'660093',1,'AS38266 Vodafone Idea Ltd'),(63,'ss','','ss','','',2,'660093',2,'AS38266 Vodafone Idea Ltd'),(64,'Who is the father of C language?','Steve Jobs','James Gosling','Dennis Ritchie','Rasmus Lerdorf',3,'100120',1,'AS55836 Reliance Jio Infocomm Limited'),(65,'All keywords in C are in?','LowerCase letters','UpperCase letters','CamelCase letters','nan',1,'100120',2,'AS55836 Reliance Jio Infocomm Limited'),(66,'What is an example of iteration in C?','for','while','do-while','all',4,'100120',3,'AS55836 Reliance Jio Infocomm Limited'),(67,'We cannot use the keyword ‘break’ simply within?','while','for','if-else','do-while',3,'100120',4,'AS55836 Reliance Jio Infocomm Limited'),(68,'The global variables are ?','External','Internal','Both External and Internal','nan',1,'100120',5,'AS55836 Reliance Jio Infocomm Limited'),(69,'Who is the father of C language?','Steve Jobs','James Gosling','Dennis Ritchie','Rasmus Lerdorf',3,'759441',1,'AS55836 Reliance Jio Infocomm Limited'),(70,'All keywords in C are in?','LowerCase letters','UpperCase letters','CamelCase letters','nan',1,'759441',2,'AS55836 Reliance Jio Infocomm Limited'),(71,'What is an example of iteration in C?','for','while','do-while','all',4,'759441',3,'AS55836 Reliance Jio Infocomm Limited'),(72,'We cannot use the keyword ‘break’ simply within?','while','for','if-else','do-while',3,'759441',4,'AS55836 Reliance Jio Infocomm Limited'),(73,'The global variables are ?','External','Internal','Both External and Internal','nan',1,'759441',5,'AS55836 Reliance Jio Infocomm Limited'),(74,'Who is the father of C language?','Steve Jobs','James Gosling','Dennis Ritchie','Rasmus Lerdorf',3,'524384',1,'AS38266 Vodafone Idea Ltd'),(75,'All keywords in C are in?','LowerCase letters','UpperCase letters','CamelCase letters','nan',1,'524384',2,'AS38266 Vodafone Idea Ltd'),(76,'What is an example of iteration in C?','for','while','do-while','all',4,'524384',3,'AS38266 Vodafone Idea Ltd'),(77,'We cannot use the keyword ‘break’ simply within?','while','for','if-else','do-while',3,'524384',4,'AS38266 Vodafone Idea Ltd'),(78,'The global variables are ?','External','Internal','Both External and Internal','nan',1,'524384',5,'AS38266 Vodafone Idea Ltd'),(79,'dihiwhw','','dwdwdw','','',2,'146175',1,'AS38266 Vodafone Idea Ltd'),(80,'fwfwfwf','','fwf','','',2,'146175',2,'AS38266 Vodafone Idea Ltd'),(81,'Who is the father of C language?','Steve Jobs','James Gosling','Dennis Ritchie','Rasmus Lerdorf',3,'782070',1,'AS38266 Vodafone Idea Ltd'),(82,'All keywords in C are in?','LowerCase letters','UpperCase letters','CamelCase letters','nan',1,'782070',2,'AS38266 Vodafone Idea Ltd'),(83,'What is an example of iteration in C?','for','while','do-while','all',4,'782070',3,'AS38266 Vodafone Idea Ltd'),(84,'We cannot use the keyword ‘break’ simply within?','while','for','if-else','do-while',3,'782070',4,'AS38266 Vodafone Idea Ltd'),(85,'The global variables are ?','External','Internal','Both External and Internal','nan',1,'782070',5,'AS38266 Vodafone Idea Ltd');
/*!40000 ALTER TABLE `quiz_que` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-02 15:25:43
