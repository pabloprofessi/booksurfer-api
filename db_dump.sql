-- MySQL dump 10.13  Distrib 5.7.16, for Linux (x86_64)
--
-- Host: 172.17.0.2    Database: booksurfer
-- ------------------------------------------------------
-- Server version	5.7.14

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `booksurfer`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `booksurfer` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `booksurfer`;

--
-- Table structure for table `author`
--

DROP TABLE IF EXISTS `author`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `author` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `nationality` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `author`
--

LOCK TABLES `author` WRITE;
/*!40000 ALTER TABLE `author` DISABLE KEYS */;
INSERT INTO `author` VALUES (2,'Pablo','Professi','Åland Islands'),(3,'Javier','Anselmi','Åland Islands'),(4,'Kuasimodo','Borbonete','Åland Islands'),(5,'Quintaro','Grindustre','Albania'),(6,'Gonzo','Bonneli','Åland Islands'),(7,'Ratimi','Tipipio','Australia'),(8,'Pituzete','Gibraltar','Australia');
/*!40000 ALTER TABLE `author` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `book`
--

DROP TABLE IF EXISTS `book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `book` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) DEFAULT NULL,
  `publisher` varchar(200) DEFAULT NULL,
  `edition_year` int(11) DEFAULT NULL,
  `edition_country` varchar(64) DEFAULT NULL,
  `price` float DEFAULT NULL,
  `isbn` varchar(13) DEFAULT NULL,
  `gender` varchar(100) DEFAULT NULL,
  `reputation_value` float DEFAULT NULL,
  `erased` tinyint(1) DEFAULT NULL,
  `loan_type` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book`
--

LOCK TABLES `book` WRITE;
/*!40000 ALTER TABLE `book` DISABLE KEYS */;
INSERT INTO `book` VALUES (1,'Alfajores','planeta',2010,'Australia',10.5,'1234567890','terror',7,0,'REMOTE'),(2,'123123','123123',123,'Albania',1233,'1231','12312',1,1,'REMOTE'),(3,'El ciervo del alma','planeta',2010,'Aruba',10.5,'11111111111','terror',6,0,'REMOTE'),(4,'El señor de los anillos - Las dos torres','planeta',2010,'Aruba',100,'2128629716','fisica',6,0,'REMOTE'),(5,'Harry Potter y la piedra filosofal','planeta',2010,'Austria',200,'3029855590','fisica',8,0,'LOCAL'),(6,'pacman trumpeterio','emeces',2011,'Bangladesh',1000,'23329321991','suspenso',5,1,'REMOTE'),(7,'La piedra en el estanque','golondrina',2010,'Azerbaijan',10.5,'1621017673','terror',6,0,'REMOTE'),(8,'Jefatura del Bebe Gloglo','salamndra',2010,'Bahamas',10.5,'2649520825','Infantil',3,0,'REMOTE');
/*!40000 ALTER TABLE `book` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `books_author`
--

DROP TABLE IF EXISTS `books_author`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `books_author` (
  `book_id` int(11) NOT NULL,
  `author_id` int(11) NOT NULL,
  PRIMARY KEY (`book_id`,`author_id`),
  KEY `author_id` (`author_id`),
  CONSTRAINT `books_author_ibfk_1` FOREIGN KEY (`book_id`) REFERENCES `book` (`id`),
  CONSTRAINT `books_author_ibfk_2` FOREIGN KEY (`author_id`) REFERENCES `author` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books_author`
--

LOCK TABLES `books_author` WRITE;
/*!40000 ALTER TABLE `books_author` DISABLE KEYS */;
INSERT INTO `books_author` VALUES (4,2),(3,3),(4,3),(5,3),(5,4),(4,5),(5,5),(3,7),(3,8),(5,8);
/*!40000 ALTER TABLE `books_author` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loan`
--

DROP TABLE IF EXISTS `loan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `loan` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `member_id` int(11) NOT NULL,
  `sample_id` int(11) NOT NULL,
  `agreed_return_date` date DEFAULT NULL,
  `return_date` date DEFAULT NULL,
  `withdraw_date` date DEFAULT NULL,
  `comment` text,
  `loan_type` varchar(10) DEFAULT NULL,
  `display` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `member_id` (`member_id`),
  KEY `sample_id` (`sample_id`),
  CONSTRAINT `loan_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `member` (`id`),
  CONSTRAINT `loan_ibfk_2` FOREIGN KEY (`sample_id`) REFERENCES `sample` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loan`
--

LOCK TABLES `loan` WRITE;
/*!40000 ALTER TABLE `loan` DISABLE KEYS */;
INSERT INTO `loan` VALUES (1,1,1,'2016-11-09','2016-10-29','2016-10-28','fghfghg','REMOTE','DISPLAY'),(2,1,1,'2016-11-10',NULL,'2016-10-29',NULL,'REMOTE','DISPLAY'),(3,1,10,'2016-11-08','2016-11-08','2016-11-07','esl pibe es macanudo','LOCAL','DISPLAY'),(4,2,4,'2016-11-19','2016-11-08','2016-11-07','kerni pasion','REMOTE','DISPLAY'),(5,2,8,'2016-11-19',NULL,'2016-11-07',NULL,'REMOTE','DISPLAY'),(6,1,4,'2016-11-09',NULL,'2016-11-08',NULL,'LOCAL','DISPLAY'),(7,3,14,'2016-09-05',NULL,'2016-08-24',NULL,'REMOTE','DISPLAY'),(8,4,16,'2015-09-05',NULL,'2015-08-24',NULL,'REMOTE','DISPLAY');
/*!40000 ALTER TABLE `loan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `member`
--

DROP TABLE IF EXISTS `member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `member` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `dni` varchar(16) DEFAULT NULL,
  `nationality` varchar(50) DEFAULT NULL,
  `cuil` varchar(24) DEFAULT NULL,
  `phone` varchar(24) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `zip_code` varchar(10) DEFAULT NULL,
  `city` varchar(100) DEFAULT NULL,
  `state` varchar(100) DEFAULT NULL,
  `enabled` tinyint(1) DEFAULT NULL,
  `reputation` float DEFAULT NULL,
  `erased` tinyint(1) DEFAULT NULL,
  `authorized_to_loan` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member`
--

LOCK TABLES `member` WRITE;
/*!40000 ALTER TABLE `member` DISABLE KEYS */;
INSERT INTO `member` VALUES (1,'Nicolas','Medina','35675119','Azerbaijan','20-2142414212-2','1566767762','jaaaa@gmail.com','1234','Batán','Jujuy',1,0,0,1),(2,'Juan','Gómez','34343434','Nigeria','20-34343434-2','12213123123','juan@xn--qweqw-j7a.com','1602','Benavídez','San Luis',1,0,0,1),(3,'Hernán','Navidad','35765089','Åland Islands','20-35765089-2','47098765','aaa@aaa.com','1312','Alberti','Chaco',1,0,0,1),(4,'Maldivas','Pancarta','19201912','Albania','20-19201912-2','31212432','ewqe@aa.com','1603','Alejandro Korn','Corrientes',1,0,0,1);
/*!40000 ALTER TABLE `member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `publisher`
--

DROP TABLE IF EXISTS `publisher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `publisher` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `publisher`
--

LOCK TABLES `publisher` WRITE;
/*!40000 ALTER TABLE `publisher` DISABLE KEYS */;
INSERT INTO `publisher` VALUES (3,'Planeta'),(4,'Penguin'),(5,'Golondrina'),(6,'Emc'),(7,'Salamandra');
/*!40000 ALTER TABLE `publisher` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sample`
--

DROP TABLE IF EXISTS `sample`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sample` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `book_id` int(11) NOT NULL,
  `acquisition_date` date DEFAULT NULL,
  `discard_date` date DEFAULT NULL,
  `bar_code` varchar(32) DEFAULT NULL,
  `erased` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `book_id` (`book_id`),
  CONSTRAINT `sample_ibfk_1` FOREIGN KEY (`book_id`) REFERENCES `book` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sample`
--

LOCK TABLES `sample` WRITE;
/*!40000 ALTER TABLE `sample` DISABLE KEYS */;
INSERT INTO `sample` VALUES (1,1,'2010-10-22',NULL,'1234567890',0),(2,2,'2016-10-30',NULL,'12332123123',1),(3,2,'2016-10-30',NULL,'12332123124',1),(4,1,'2016-10-13',NULL,'12312312',0),(5,1,'2016-10-21','2016-09-14','123123123',0),(6,6,'2016-11-09',NULL,'2833318619',1),(7,6,'2016-10-12',NULL,'5046154560',1),(8,5,'2016-10-04',NULL,'5619110240',0),(9,5,'2016-11-01',NULL,'5619110222',0),(10,4,'2016-03-09',NULL,'2520517430',0),(11,3,'2016-11-16',NULL,'11111111',0),(12,3,'2016-11-12','2016-11-25','22222222',0),(13,3,'2016-11-24','2016-11-07','33333333',0),(14,3,'2016-11-18',NULL,'44444444',0),(15,4,'2016-11-15',NULL,'555555555',0),(16,7,'2016-11-25',NULL,'56756756',0),(17,8,'2017-02-06',NULL,'1234567110',0),(18,1,'2017-02-06',NULL,'1234567220',0);
/*!40000 ALTER TABLE `sample` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `role` varchar(10) DEFAULT NULL,
  `dni` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (2,'Martin','Remondini','martin','martin','ADMIN','35675890'),(3,'Hernan','Pascua','hernan','hernan','ADMIN','35435435'),(4,'Ludovico','Sarchi','ludovico','ludovico','SUPERVISOR','35435435'),(5,'Patricio','Manzato','patricio','patricio','SUPERVISOR','16780938');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Current Database: `booksurfer`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `booksurfer` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `booksurfer`;

--
-- Table structure for table `author`
--

DROP TABLE IF EXISTS `author`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `author` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `nationality` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `author`
--

LOCK TABLES `author` WRITE;
/*!40000 ALTER TABLE `author` DISABLE KEYS */;
INSERT INTO `author` VALUES (2,'Pablo','Professi','Åland Islands'),(3,'Javier','Anselmi','Åland Islands'),(4,'Kuasimodo','Borbonete','Åland Islands'),(5,'Quintaro','Grindustre','Albania'),(6,'Gonzo','Bonneli','Åland Islands'),(7,'Ratimi','Tipipio','Australia'),(8,'Pituzete','Gibraltar','Australia');
/*!40000 ALTER TABLE `author` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `book`
--

DROP TABLE IF EXISTS `book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `book` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) DEFAULT NULL,
  `publisher` varchar(200) DEFAULT NULL,
  `edition_year` int(11) DEFAULT NULL,
  `edition_country` varchar(64) DEFAULT NULL,
  `price` float DEFAULT NULL,
  `isbn` varchar(13) DEFAULT NULL,
  `gender` varchar(100) DEFAULT NULL,
  `reputation_value` float DEFAULT NULL,
  `erased` tinyint(1) DEFAULT NULL,
  `loan_type` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book`
--

LOCK TABLES `book` WRITE;
/*!40000 ALTER TABLE `book` DISABLE KEYS */;
INSERT INTO `book` VALUES (1,'Alfajores','planeta',2010,'Australia',10.5,'1234567890','terror',7,0,'REMOTE'),(2,'123123','123123',123,'Albania',1233,'1231','12312',1,1,'REMOTE'),(3,'El ciervo del alma','planeta',2010,'Aruba',10.5,'11111111111','terror',6,0,'REMOTE'),(4,'El señor de los anillos - Las dos torres','planeta',2010,'Aruba',100,'2128629716','fisica',6,0,'REMOTE'),(5,'Harry Potter y la piedra filosofal','planeta',2010,'Austria',200,'3029855590','fisica',8,0,'LOCAL'),(6,'pacman trumpeterio','emeces',2011,'Bangladesh',1000,'23329321991','suspenso',5,1,'REMOTE'),(7,'La piedra en el estanque','golondrina',2010,'Azerbaijan',10.5,'1621017673','terror',6,0,'REMOTE'),(8,'Jefatura del Bebe Gloglo','salamndra',2010,'Bahamas',10.5,'2649520825','Infantil',3,0,'REMOTE');
/*!40000 ALTER TABLE `book` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `books_author`
--

DROP TABLE IF EXISTS `books_author`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `books_author` (
  `book_id` int(11) NOT NULL,
  `author_id` int(11) NOT NULL,
  PRIMARY KEY (`book_id`,`author_id`),
  KEY `author_id` (`author_id`),
  CONSTRAINT `books_author_ibfk_1` FOREIGN KEY (`book_id`) REFERENCES `book` (`id`),
  CONSTRAINT `books_author_ibfk_2` FOREIGN KEY (`author_id`) REFERENCES `author` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books_author`
--

LOCK TABLES `books_author` WRITE;
/*!40000 ALTER TABLE `books_author` DISABLE KEYS */;
INSERT INTO `books_author` VALUES (4,2),(3,3),(4,3),(5,3),(5,4),(4,5),(5,5),(3,7),(3,8),(5,8);
/*!40000 ALTER TABLE `books_author` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loan`
--

DROP TABLE IF EXISTS `loan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `loan` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `member_id` int(11) NOT NULL,
  `sample_id` int(11) NOT NULL,
  `agreed_return_date` date DEFAULT NULL,
  `return_date` date DEFAULT NULL,
  `withdraw_date` date DEFAULT NULL,
  `comment` text,
  `loan_type` varchar(10) DEFAULT NULL,
  `display` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `member_id` (`member_id`),
  KEY `sample_id` (`sample_id`),
  CONSTRAINT `loan_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `member` (`id`),
  CONSTRAINT `loan_ibfk_2` FOREIGN KEY (`sample_id`) REFERENCES `sample` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loan`
--

LOCK TABLES `loan` WRITE;
/*!40000 ALTER TABLE `loan` DISABLE KEYS */;
INSERT INTO `loan` VALUES (1,1,1,'2016-11-09','2016-10-29','2016-10-28','fghfghg','REMOTE','DISPLAY'),(2,1,1,'2016-11-10',NULL,'2016-10-29',NULL,'REMOTE','DISPLAY'),(3,1,10,'2016-11-08','2016-11-08','2016-11-07','esl pibe es macanudo','LOCAL','DISPLAY'),(4,2,4,'2016-11-19','2016-11-08','2016-11-07','kerni pasion','REMOTE','DISPLAY'),(5,2,8,'2016-11-19',NULL,'2016-11-07',NULL,'REMOTE','DISPLAY'),(6,1,4,'2016-11-09',NULL,'2016-11-08',NULL,'LOCAL','DISPLAY'),(7,3,14,'2016-09-05',NULL,'2016-08-24',NULL,'REMOTE','DISPLAY'),(8,4,16,'2015-09-05',NULL,'2015-08-24',NULL,'REMOTE','DISPLAY');
/*!40000 ALTER TABLE `loan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `member`
--

DROP TABLE IF EXISTS `member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `member` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `dni` varchar(16) DEFAULT NULL,
  `nationality` varchar(50) DEFAULT NULL,
  `cuil` varchar(24) DEFAULT NULL,
  `phone` varchar(24) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `zip_code` varchar(10) DEFAULT NULL,
  `city` varchar(100) DEFAULT NULL,
  `state` varchar(100) DEFAULT NULL,
  `enabled` tinyint(1) DEFAULT NULL,
  `reputation` float DEFAULT NULL,
  `erased` tinyint(1) DEFAULT NULL,
  `authorized_to_loan` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member`
--

LOCK TABLES `member` WRITE;
/*!40000 ALTER TABLE `member` DISABLE KEYS */;
INSERT INTO `member` VALUES (1,'Nicolas','Medina','35675119','Azerbaijan','20-2142414212-2','1566767762','jaaaa@gmail.com','1234','Batán','Jujuy',1,0,0,1),(2,'Juan','Gómez','34343434','Nigeria','20-34343434-2','12213123123','juan@xn--qweqw-j7a.com','1602','Benavídez','San Luis',1,0,0,1),(3,'Hernán','Navidad','35765089','Åland Islands','20-35765089-2','47098765','aaa@aaa.com','1312','Alberti','Chaco',1,0,0,1),(4,'Maldivas','Pancarta','19201912','Albania','20-19201912-2','31212432','ewqe@aa.com','1603','Alejandro Korn','Corrientes',1,0,0,1);
/*!40000 ALTER TABLE `member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `publisher`
--

DROP TABLE IF EXISTS `publisher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `publisher` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `publisher`
--

LOCK TABLES `publisher` WRITE;
/*!40000 ALTER TABLE `publisher` DISABLE KEYS */;
INSERT INTO `publisher` VALUES (3,'Planeta'),(4,'Penguin'),(5,'Golondrina'),(6,'Emc'),(7,'Salamandra');
/*!40000 ALTER TABLE `publisher` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sample`
--

DROP TABLE IF EXISTS `sample`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sample` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `book_id` int(11) NOT NULL,
  `acquisition_date` date DEFAULT NULL,
  `discard_date` date DEFAULT NULL,
  `bar_code` varchar(32) DEFAULT NULL,
  `erased` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `book_id` (`book_id`),
  CONSTRAINT `sample_ibfk_1` FOREIGN KEY (`book_id`) REFERENCES `book` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sample`
--

LOCK TABLES `sample` WRITE;
/*!40000 ALTER TABLE `sample` DISABLE KEYS */;
INSERT INTO `sample` VALUES (1,1,'2010-10-22',NULL,'1234567890',0),(2,2,'2016-10-30',NULL,'12332123123',1),(3,2,'2016-10-30',NULL,'12332123124',1),(4,1,'2016-10-13',NULL,'12312312',0),(5,1,'2016-10-21','2016-09-14','123123123',0),(6,6,'2016-11-09',NULL,'2833318619',1),(7,6,'2016-10-12',NULL,'5046154560',1),(8,5,'2016-10-04',NULL,'5619110240',0),(9,5,'2016-11-01',NULL,'5619110222',0),(10,4,'2016-03-09',NULL,'2520517430',0),(11,3,'2016-11-16',NULL,'11111111',0),(12,3,'2016-11-12','2016-11-25','22222222',0),(13,3,'2016-11-24','2016-11-07','33333333',0),(14,3,'2016-11-18',NULL,'44444444',0),(15,4,'2016-11-15',NULL,'555555555',0),(16,7,'2016-11-25',NULL,'56756756',0),(17,8,'2017-02-06',NULL,'1234567110',0),(18,1,'2017-02-06',NULL,'1234567220',0);
/*!40000 ALTER TABLE `sample` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `role` varchar(10) DEFAULT NULL,
  `dni` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (2,'Martin','Remondini','martin','martin','ADMIN','35675890'),(3,'Hernan','Pascua','hernan','hernan','ADMIN','35435435'),(4,'Ludovico','Sarchi','ludovico','ludovico','SUPERVISOR','35435435'),(5,'Patricio','Manzato','patricio','patricio','SUPERVISOR','16780938');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-02-06 23:07:31
