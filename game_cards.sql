-- MySQL dump 10.13  Distrib 8.0.16, for Win64 (x86_64)
--
-- Host: localhost    Database: game
-- ------------------------------------------------------
-- Server version	8.0.16

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cards`
--

DROP TABLE IF EXISTS `cards`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `cards` (
  `idcards` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `faction` varchar(45) DEFAULT NULL,
  `rarity` varchar(45) DEFAULT NULL,
  `display` varchar(45) DEFAULT NULL,
  `attack` int(11) DEFAULT NULL,
  `health` int(11) DEFAULT NULL,
  `cost` int(11) unsigned DEFAULT NULL,
  `sleep` int(11) unsigned DEFAULT '1',
  `trap` tinyint(3) unsigned DEFAULT '0',
  `marksmen` tinyint(3) unsigned DEFAULT '0',
  `carrier` tinyint(4) unsigned DEFAULT '0',
  `dodge` int(10) unsigned DEFAULT '0',
  `stealth` int(10) unsigned DEFAULT '0',
  `bloodbath` int(10) unsigned DEFAULT '0',
  `enchant` int(10) unsigned DEFAULT '0',
  `legacy` int(10) unsigned DEFAULT '0',
  `armor` int(10) unsigned DEFAULT '0',
  `castle` int(10) unsigned DEFAULT '0',
  `anesthetize` int(10) unsigned DEFAULT '0',
  `draw` int(10) unsigned DEFAULT '0',
  PRIMARY KEY (`idcards`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cards`
--

LOCK TABLES `cards` WRITE;
/*!40000 ALTER TABLE `cards` DISABLE KEYS */;
INSERT INTO `cards` VALUES (1,'Air Drone','Machine','starter','ad',1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0),(2,'Bomb Trap','Machine','starter','bt',0,2,1,1,1,0,0,0,0,0,0,0,0,0,0,0),(3,'Sniper','Machine','common','sn',1,1,1,1,0,3,0,0,0,0,0,0,0,0,0,0),(4,'Collosus','Machine','common','co',4,4,2,1,0,0,0,0,0,0,0,0,0,0,0,0),(5,'Botbox','Machine','common','bb',0,4,1,1,0,0,1,0,0,0,0,0,0,0,0,0),(6,'Kobold Warrior','Neutral','token','kw',1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0),(7,'Pixie','Fey','starter','pi',1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0),(8,'Naga Assassin','Aliance','common','na',3,1,1,1,0,0,0,0,1,1,0,0,0,0,0,0),(9,'Pixie Acolyte','Fey','starter','pa',1,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0),(10,'Pixie Knight','Fey','common','pk',2,2,1,1,0,0,0,0,0,0,0,1,0,0,0,0),(11,'Pixie Shaman','Fey','common','ps',2,1,1,1,0,0,0,0,0,0,2,0,0,0,0,0),(12,'Squaire','Aliance','common','sq',2,1,1,1,0,0,0,0,0,0,0,0,1,0,0,0),(13,'Castle','Aliance','common','ca',0,4,1,1,0,0,0,0,0,0,0,0,0,1,0,0),(14,'Wild Hunt','Fey','rare','wh',5,2,3,0,0,0,0,0,0,0,0,0,0,0,0,0),(15,'Will-o-Wisp','Fey','common','ww',2,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0),(16,'Nymph','Fey','common','ny',2,1,1,1,0,0,0,0,0,0,0,0,0,0,1,0),(17,'Pixie Hermit','Fey','rare','ph',2,1,3,1,0,0,0,0,0,0,5,0,0,0,0,0),(18,'Pot of Time','Neutral','uncommon','pt',0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,2),(19,'Dryad','Fey','uncommon','dr',4,1,2,1,0,0,0,0,0,0,0,0,0,0,1,0),(20,'Kobold Ninja','Neutral','rare','kn',3,1,1,1,0,0,0,0,1,0,0,0,0,0,0,1),(21,'Shifting Stone','Fey','uncommon','ss',0,6,2,1,0,0,0,1,0,0,2,0,0,0,0,0),(22,'Warrior','Neutral','common','wa',2,2,0,1,0,0,0,0,0,0,0,0,0,0,0,0),(23,'Zombie','Neutral','common','zo',2,2,1,1,0,0,0,0,0,0,0,1,0,0,0,0),(24,'Fun Ball','Machine','rare','fb',0,1,1,1,3,0,0,0,0,0,0,1,0,0,0,0),(25,'Starship','Machine','uncommon','st',2,3,2,1,0,2,2,0,0,0,0,0,0,0,0,0),(26,'Explosive Decoy','Machine','uncommon','ed',0,5,2,1,2,0,0,0,0,0,0,0,0,1,0,0);
/*!40000 ALTER TABLE `cards` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-06-14 16:14:29
