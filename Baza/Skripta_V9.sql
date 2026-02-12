SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;


CREATE DATABASE IF NOT EXISTS `StolariDB` DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;
USE `StolariDB`;



DROP TABLE IF EXISTS `Admin`;
CREATE TABLE `Admin`
(
    `IdAdmin` integer NOT NULL AUTO_INCREMENT,
    `Username` varchar(40) NOT NULL,
    `Password` varchar(40) NOT NULL,
    PRIMARY KEY (`IdAdmin`)
);


INSERT INTO `Admin` (`IdAdmin`, `Username`, `Password`) VALUES
(1, 'admin', 'admin1234');


DROP TABLE IF EXISTS `Galerija`;
CREATE TABLE `Galerija`
(
    `IdSlika` integer NOT NULL AUTO_INCREMENT,
    `Path` varchar(255) NOT NULL ,
    `TipSlike` varchar(1) NOT NULL ,
     `IdObj` integer NULL ,
     `IdVest`integer NULL,
     PRIMARY KEY (`IdSlika`),
     KEY `IdObj`(`IdObj`),
     KEY `IdVest`(`IdVest`)
);


INSERT INTO `Galerija` (`IdSlika`, `Path`, `TipSlike`, `IdObj`, `IdVest`) VALUES
(1, 'slike/Insolita.jpg', 'C', 1, NULL),
(2, 'slike/Insolita2.jpg', 'O', 1, NULL),
(3, 'slike/menu_insolita.png', 'M', 1, NULL),
(4, 'slike/insolita-rp.jpg', 'P', 1, NULL),
(5, 'slike/restoran_city_garden_1.jpg', 'C', 2, NULL),
(6, 'slike/cityGarden.jpg', 'O', 2, NULL),
(7, 'slike/meni_city_garden.jpg', 'M', 2, NULL),
(8, 'slike/cityGarden-rp.jpeg', 'P', 2, NULL),
(9, 'slike/bahusInn.jpg', 'C', 3, NULL),
(10, 'slike/bahus-inn-restoran-1.jpg', 'O', 3, NULL),
(11, 'slike/bahus-in-menu.jpg', 'M', 3, NULL),
(12, 'slike/bahusInn-rp.jpg', 'P', 3, NULL),
(13, 'slike/inbox.jpg', 'C', 4, NULL),
(14, 'slike/inbox2.jpg', 'O', 4, NULL),
(15, 'slike/kartapica-inbox.jpg', 'M', 4, NULL),
(16, 'slike/inbox-rp.jpeg', 'P', 4, NULL),
(17, 'slike/witchBar.jpg', 'C', 5, NULL),
(18, 'slike/witch_bar_1.jpeg', 'O', 5, NULL),
(19, 'slike/witch_bar_karta_pica.jpg', 'M', 5, NULL),
(20, 'slike/witchBar-rp.jpeg', 'P', 5, NULL),
(21, 'slike/Insolita-tables.png', 'S', 1, NULL),
(22, 'slike/bahusInn-tables.png', 'S', 3, NULL),
(23, 'slike/cityGarden-tables.png', 'S', 2, NULL),
(24, 'slike/inBox-tables.jpg', 'S', 4, NULL),
(25, 'slike/witchBar-tables.jpg', 'S', 5, NULL);



DROP TABLE IF EXISTS `Iznajmljivanje`;
CREATE TABLE `Iznajmljivanje`
(
   `IdIzn`integer NOT NULL AUTO_INCREMENT,
   `DatumPocetka` date NOT NULL ,
   `VremePocetka` time NOT NULL ,
   `DatumKraja` date NOT NULL ,
   `VremeKraja` time NOT NULL ,
   `Status` varchar(40) NOT NULL ,
   `IdObj` integer NOT NULL ,
   `IdrReg` integer NOT NULL,
   PRIMARY KEY(`IdIzn`),
   KEY `IdObj`(`IdObj`),
   KEY `IdrReg`(`IdrReg`)
);


INSERT INTO `Iznajmljivanje`(`IdIzn`, `DatumPocetka`,`VremePocetka`,`DatumKraja`,`VremeKraja`, `Status`, `IdObj`, `IdrReg`) VALUES
(1, '2023-03-08','14:00','2023-03-08','15:00', 'ostvaren', 1, 1),
(2, '2023-03-12','21:00','2023-03-12','23:00', 'neostvaren', 1, 2),
(3, '2023-06-28','20:50','2023-06-28','23:50', 'unmarked', 2, 1);


DROP TABLE IF EXISTS `Omiljeni`;
CREATE TABLE `Omiljeni`
(
    `IdOmilj` integer NOT NULL AUTO_INCREMENT,
    `IdrReg` integer NOT NULL,
    `IdObj` integer NOT NULL,
    PRIMARY KEY(`IdOmilj`),
    KEY `IdrReg`(`IdrReg`),
    KEY `IdObj`(`IdObj`)
);
INSERT INTO `Omiljeni`(`IdOmilj`,`IdrReg`, `IdObj`) VALUES
(1, 1, 2),
(2, 1, 3);

DROP TABLE IF EXISTS `Rezervacija`;
CREATE TABLE `Rezervacija`
( 
	`IdRez`             integer  NOT NULL AUTO_INCREMENT,
	`DatumPocetka` 		date NOT NULL ,
    `VremePocetka` 		time NOT NULL ,
    `DatumKraja` 		date NOT NULL ,
    `VremeKraja` 		time NOT NULL ,
	`Status`            varchar(40)  NOT NULL ,
	`IdSto`             integer  NOT NULL ,
	`IdrReg`            integer  NOT NULL ,
    `IdObj`             integer  NOT NULL ,
    PRIMARY KEY(`IdRez`),
    KEY `IdSto`(`IdSto`),
    KEY `IdrReg`(`IdrReg`),
    KEY `IdObj`(`IdObj`)
);
INSERT INTO `Rezervacija`(`IdRez`, `DatumPocetka`,`VremePocetka`,`DatumKraja`,`VremeKraja`, `Status`, `IdSto`, `IdrReg`,`IdObj`) VALUES
(1, '2023-07-15','14:00','2023-07-15','16:00', 'ostvaren', 1, 1, 1),
(2, '2023-07-20','14:00','2023-07-20','15:00', 'neostvaren', 2, 1, 1),
(3, '2023-07-25','14:00','2023-07-25','15:00', 'ostvaren', 50, 1, 5);

DROP TABLE IF EXISTS `Sto`;
CREATE TABLE `Sto`
( 
	`IdSto`              integer  NOT NULL AUTO_INCREMENT,
	`IdObj`              integer  NOT NULL ,
	`IdTip`              integer  NOT NULL ,
    PRIMARY KEY(`IdSto`),
    KEY `IdObj`(`IdObj`),
    KEY `IdTip`(`IdTip`)
);

INSERT INTO `Sto`(`IdSto`, `IdObj`, `IdTip`) VALUES
(1, 1, 1),
(2, 1, 1),
(3, 1, 2),
(4, 1, 2),
(5, 1, 1),
(6, 1, 3),
(7, 1, 2),
(8, 1, 3),
(9, 1, 3),
(10, 2, 1),
(11, 2, 1),
(12, 2, 2),
(13, 2, 2),
(14, 2, 1),
(15, 2, 3),
(16, 2, 2),
(17, 2, 3),
(18, 2, 3),
(19, 3, 1),
(20, 3, 1),
(21, 3, 2),
(22, 3, 2),
(23, 3, 1),
(24, 3, 3),
(25, 3, 2),
(26, 3, 3),
(27, 3, 3),
(28, 4, 4),
(29, 4, 4),
(30, 4, 5),
(31, 4, 6),
(32, 4, 5),
(33, 4, 4),
(34, 4, 5),
(35, 4, 6),
(36, 4, 4),
(37, 4, 5),
(38, 4, 5),
(39, 4, 6),
(40, 4, 4),
(41, 4, 4),
(42, 4, 4),
(43, 4, 4),
(44, 4, 4),
(45, 4, 5),
(46, 4, 6),
(47, 4, 6),
(48, 5, 7),
(49, 5, 8),
(50, 5, 9),
(51, 5, 7),
(52, 5, 8),
(53, 5, 9);


DROP TABLE IF EXISTS `Objekat`;
CREATE TABLE `Objekat`
( 
	`IdObj`              integer  NOT NULL AUTO_INCREMENT,
	`Naziv`              varchar(40)  NOT NULL ,
	`Adresa`             varchar(40)  NOT NULL ,
	`Grad`               varchar(40)  NOT NULL ,
	`TipObj`			 varchar(40)  NOT NULL ,
	`TipKuhinje`         varchar(40)  NOT NULL ,
	`UkOcena`            integer  NOT NULL ,
	`BrOcena`            integer  NOT NULL ,
    `Opis`			     varchar(1000) NOT NULL,
	`IdMen`              integer  NOT NULL ,
    PRIMARY KEY(`IdObj`),
    KEY `IdMen`(`IdMen`)
);

INSERT INTO `Objekat`(`IdObj`, `Naziv`, `Adresa`, `Grad`, `TipObj`, `TipKuhinje`, `UkOcena`, `BrOcena`, `Opis`, `IdMen`) VALUES
(1, 'Insolita', 'Zorza Klemensoa 27v', 'Nis', 'restoran', 'italian', 15, 6, 'Insolita je upravo omaz lucidnosti i domisljatosti italijanske kuhinje. Istovremeno tradicionalna i uvek spremna za novo, nesvakidasnje, neuobicajeno i van utabanog puta. Spremna da bude mlada kad krenete u grad, kao i da pokaze svoje anticke korene u bakinom receptu.
      Insolita uzima sve te ideje od Kalabrije do Frijulija, od Toskane do Sicilije, od jelovnika u zabacenim ulicicama Palerma ili Napulja do bezbroj varijacija tih istih jela na putu za Torino ili Udine.
      Rastavlja ih i ponovo sastavlja, trazeci savrsen odnos punoce, teksture i boje, kvaliteta i zdravlja, inspiracije i gastronomskog dozivljaja.', 1),
(2, 'City Garden', 'Knez Mihailova 54', 'Beograd', 'restoran', 'serbian', 20, 4, ' Beograd, u svom punom sjaju, najbolje možete doživeti kroz kombinaciju hrane, vina i najboljeg pogleda koji Vam centar pruža! Uživajte na terasi našeg restorana, a tokom zimskih dana za one koji vole ušuškanost – naša zastakljena terasa je pravi raj.
        Pogled se pruža na Sabornu Crkvu, Knez Mihailovu ulicu, Kalemegdan, ušće Save u Dunav, Sahat kulu, pa sve do mosta na Adi.
        Savršeno mesto za predah i uživanje.Kod nas možete ostvariti sve Vaše želje, jer smo mi Vaša savršena lokacija za realizaciju svih vrsta događaja.
        Na Vama je da odaberete datum i meni, a na nama je da svaki sastojak bude perfektno odmeren i svaki gram ukusa pažljivo ukombinovan.
        Muzika, ples, simfonija ukusa, savršena usluga i Vaš lični event menadžer – sve na jednom mestu!
        Neka sve bude stvoreno baš po Vašim željama.' , 2),
(3, 'Bahus Inn', 'Bulevar Nikole Tesle bb', 'Beograd', 'restoran', 'serbian', 20, 5, 'Ranih 90ih godina jedan od prvih splavova-restorana na vodi iza hotela Jugoslavije osvežio je ugostiteljsko turističku ponudu grada, ugostio je brojne poznate ličnosti iz oblasti kulture, sporta i politike, preživeo je burne političko ekonomske krize, devalvaciju, rat, bombardovanje i opstao pružajući uvek kvalitetnu uslugu i kvalitetnu hranu iz svoje ponude.
        Posle pauze od nekoliko godina Bahus danas prerasta u Bahus Inn, kao novina pružajući gostima neprevaziđene usluge smeštaja i ishrane. Bahus danas raspolaže sa 8 lux apartmana opremljenih sa najsavremenijom opremom, nameštajem, i eko posteljinom, svaki apartman je zasebna priča koja pruža iste ali u isto vreme različite usluge komfora, od masažnog đakuzi bazena do saune i prostranih terasa s prelepim pogledom na Dunav.
        Nalazi se u najlepšem delu Beograda, na ušću Save u Dunav, u neposrednoj blizini biznis centara, tržnih centara i kulturno istorijskih objekata kojima obiluje grad.', 1),
(4, 'InBox', 'Karadjordjeva 9', 'Beograd', 'klub', '/', 20, 6, 'Jedan od omiljenih klupskih prostora Beograđana sa dugom tradicijom kvalitetnih noćnih provoda dobio je novo ruho i pompezno najavljuje predstojeću zimsku sezonu.
        U boemskoj zoni Beograda, na mestu gde se nekada nalazio čuveni Box, otvorio se klub InBox koji će nastaviti misiju slavnih prethodnika!
        Za vrlo kratko vreme, nakon otvaranja club InBox je uspeo da postane „must be“ mesto u gradu, sa najvećim clubberima Beograda. Klub InBox okuplja urbanu gradsku ekipu, ljude koji znaju šta znači dobar provod i kvalitetna muzika. Uz sve to, u šanku su barmeni koji će sa osmehom na licu i pozitivnom energijom ugostiti sve klabere željne fenomenalnog izlaska.' , 3),
(5, 'Witch Bar', 'Pariska 13', 'Novi Sad', 'pab', '/', 20, 4, ' Witch Bar je mesto gde svačija žaba postaje princ, a ako ne bude dobar, možda i princeza! Tu svaka devojčica postaje demončica uz pomoć samo jednog gutljaja Čarobnog napitka. Verovali ili ne!
        Služimo prinčeve bez belih konja i princeze bez zrna graška, vrlo lake za održavanje - jedno pivo i već imate ljubav svog života. Ako ste mislili da se ovakve stvari dešavaju samo u bajkama, silno grešite! Ovo mesto nije u bajci, ali je iz bajke.Koktel bar je smešten u blizini Saborne Crkve i Patrijaršije, u najlepšem delu Novog Sada - Starom Gradu, sa pogledom na srednjovekovnu tvrdjavu Petrovaradin. Koktele, koji svojim zanimljivim nazivima privlače pažnju istog trena, ispijaćete sa uživanjem i oduševljenjem. Bilo da su standardni za dobar dan, ili veći od 1L i 3L za dobro veče, uticaće pozitivno na veše raspoloženje.
        Celonedeljni program i opuštena atmosfera, uz sve gore navedeno, nas čine drugačijim i boljim od ostalih.', 3);

DROP TABLE IF EXISTS `Menadzer`;
CREATE TABLE `Menadzer`
( 
	`IdMen`              integer  NOT NULL AUTO_INCREMENT,
	`Username`           varchar(40)  NOT NULL ,
	`Password`           varchar(40)  NOT NULL ,
	`Ime`                varchar(40)  NOT NULL ,
	`Prezime`            varchar(40)  NOT NULL ,
	`Pol`                varchar(40)  NOT NULL ,
	`Broj`               varchar(40)  NOT NULL ,
    PRIMARY KEY(`IdMen`)
);

INSERT INTO `Menadzer`(`IdMen`, `Username`, `Password`, `Ime`, `Prezime`, `Pol`, `Broj`) VALUES
(1, 'menadzer1', 'menadzer1234', 'Marko', 'Markovic', 'muski', '0649999999'),
(2, 'menadzer2', 'menadzer2345', 'Ivana', 'Ivanovic', 'zenski', '0648888888'),
(3, 'menadzer3', 'menadzer3456', 'Dragana', 'Mirkovic', 'zenski', '0641111111');

DROP TABLE IF EXISTS `Registrovani`;
CREATE TABLE `Registrovani`
( 
	`IdrReg`             integer  NOT NULL AUTO_INCREMENT,
	`Username`           varchar(40)  NOT NULL ,
	`Password`           varchar(40)  NOT NULL ,
	`Ime`                varchar(40)  NOT NULL ,
	`Prezime`            varchar(40)  NOT NULL ,
	`BrTelefona`         varchar(40)  NOT NULL ,
	`Pol`                varchar(40)  NOT NULL ,
	`PozPoeni`           integer  NOT NULL ,
	`NegPoeni`           integer  NOT NULL ,
	`DatumRodjenja`      datetime  NOT NULL ,
    PRIMARY KEY(`IdrReg`)
);

INSERT INTO `Registrovani`(`IdrReg`, `Username`, `Password`, `Ime`, `Prezime`, `BrTelefona`, `Pol`, `PozPoeni`, `NegPoeni`, `DatumRodjenja`) VALUES
(1, 'korisnik1', '1234', 'Pera', 'Peric', '0647777777', 'muski', 2, 1, '2000-01-09 14:00:00'),
(2, 'korisnik2', '1234', 'Djuka', 'Djukic', '0646666666', 'muski', 15, 1, '1998-01-09 15:10:00'),
(3, 'korisnik3', '1234', 'Milica', 'Banjac', '0646666666', 'zenski', 1, 20, '1998-01-09 15:10:00');




DROP TABLE IF EXISTS `Tip`;
CREATE TABLE `Tip`
( 
	`IdTip`              integer  NOT NULL AUTO_INCREMENT,
	`Naziv`              varchar(40)  NOT NULL ,
	`Opis`               varchar(40)  NOT NULL ,
    PRIMARY KEY(`IdTip`)
);

INSERT INTO `Tip`(`IdTip`, `Naziv`, `Opis`) VALUES
(1, 'restoranBarski', 'Barski sto u restoranu'),
(2, 'restoranSedenje', 'Sto za sedenje u restoranu'),
(3, 'restoranSank', 'Sank u restoranu'),
(4, 'klubBarski', 'Barski sto u klubu'),
(5, 'klubSank', 'Sank u klubu'),
(6, 'klubSepare', 'Sto u separeu u klubu'),
(7, 'pabBarski', 'Barski sto u pabu'),
(8, 'pabSedenje', 'Sto za sedenje u pabu'),
(9, 'pabSank', 'Sank u pabu');

DROP TABLE IF EXISTS `Vest`;
CREATE TABLE `Vest`
( 
	`IdVest`             integer  NOT NULL AUTO_INCREMENT,
	`Naslov`             varchar(40)  NOT NULL ,
	`Tekst`              varchar(255)  NOT NULL ,
    PRIMARY KEY(`IdVest`)
);

INSERT INTO `Vest`(`IdVest`, `Naslov`, `Tekst`) VALUES
(1, 'Uparivanje hrane i vina u Insoliti!', 'U saradnji sa vinarijom ERDEVIK, restoran Insolita Vam predstavlja prvo uparivanje hrane i vina. Rezervacije su obavezne.'),
(2, 'Novo na nasoj aplikaciji!', 'Od sada postoji mogucnost zakupljivanja celog lokala preko nase aplikacije!');




ALTER TABLE `Admin`
	ADD CONSTRAINT `XPKAdmin` PRIMARY KEY  CLUSTERED (`IdAdmin` ASC);


ALTER TABLE `Admin`
	ADD CONSTRAINT `XAK1Admin` UNIQUE (`Username`  ASC);


ALTER TABLE `Galerija`
	ADD CONSTRAINT `XPKGalerija` PRIMARY KEY  CLUSTERED (`IdSlika` ASC);


ALTER TABLE `Iznajmljivanje`
	ADD CONSTRAINT `XPKIznajmljivanje` PRIMARY KEY  CLUSTERED (`IdIzn` ASC);


ALTER TABLE `Menadzer`
	ADD CONSTRAINT `XPKMenadzer` PRIMARY KEY  CLUSTERED (`IdMen` ASC);


ALTER TABLE `Menadzer`
	ADD CONSTRAINT `XAK1Menadzer` UNIQUE (`Username`  ASC);

ALTER TABLE `Objekat`
	ADD CONSTRAINT `XPKObjekat` PRIMARY KEY  CLUSTERED (`IdObj` ASC);
    
ALTER TABLE `Omiljeni`
	ADD CONSTRAINT `XPKOmiljeni` PRIMARY KEY CLUSTERED (`IdOmilj` ASC);

ALTER TABLE `Omiljeni`
	ADD CONSTRAINT `R_1` FOREIGN KEY (`IdObj`) REFERENCES `Objekat`(`IdObj`)
		ON UPDATE CASCADE;

ALTER TABLE `Omiljeni`
	ADD CONSTRAINT `R_2` FOREIGN KEY (`IdrReg`) REFERENCES `Registrovani`(`IdrReg`)
		ON UPDATE CASCADE;


ALTER TABLE `Registrovani`
	ADD CONSTRAINT `XPKRegistrovani` PRIMARY KEY  CLUSTERED (`IdrReg` ASC);


ALTER TABLE `Registrovani`
	ADD CONSTRAINT `XAK1Registrovani` UNIQUE (`Username`  ASC);


ALTER TABLE `Rezervacija`
	ADD CONSTRAINT `XPKRezervacija` PRIMARY KEY  CLUSTERED (`IdRez` ASC);


ALTER TABLE `Sto`
	ADD CONSTRAINT `XPKSto` PRIMARY KEY  CLUSTERED (`IdSto` ASC);


ALTER TABLE `Tip`
	ADD CONSTRAINT `XPKTip` PRIMARY KEY  CLUSTERED (`IdTip` ASC);


ALTER TABLE `Vest`
	ADD CONSTRAINT `XPKVest` PRIMARY KEY  CLUSTERED (`IdVest` ASC);


ALTER TABLE `Galerija`
	ADD CONSTRAINT `R_4` FOREIGN KEY (`IdObj`) REFERENCES `Objekat`(`IdObj`)
		ON UPDATE CASCADE;

ALTER TABLE `Galerija`
	ADD CONSTRAINT `R_5` FOREIGN KEY (`IdVest`) REFERENCES `Vest`(`IdVest`)
		ON UPDATE CASCADE;



ALTER TABLE `Iznajmljivanje`
	ADD CONSTRAINT `R_10` FOREIGN KEY (`IdObj`) REFERENCES `Objekat`(`IdObj`)
		ON UPDATE CASCADE;


ALTER TABLE `Iznajmljivanje`
	ADD CONSTRAINT `R_11` FOREIGN KEY (`IdrReg`) REFERENCES `Registrovani`(`IdrReg`)
		ON UPDATE CASCADE;



ALTER TABLE `Objekat`
	ADD CONSTRAINT `R_1` FOREIGN KEY (`IdMen`) REFERENCES `Menadzer`(`IdMen`)
		ON UPDATE CASCADE;



ALTER TABLE `Omiljeni`
	ADD CONSTRAINT `R_8` FOREIGN KEY (`IdrReg`) REFERENCES `Registrovani`(`IdrReg`)
		ON UPDATE CASCADE;


ALTER TABLE `Omiljeni`
	ADD CONSTRAINT `R_9` FOREIGN KEY (`IdObj`) REFERENCES `Objekat`(`IdObj`)
		ON UPDATE CASCADE;



ALTER TABLE `Rezervacija`
	ADD CONSTRAINT `R_6` FOREIGN KEY (`IdSto`) REFERENCES `Sto`(`IdSto`)
		ON UPDATE CASCADE;


ALTER TABLE `Rezervacija`
	ADD CONSTRAINT `R_7` FOREIGN KEY (`IdrReg`) REFERENCES `Registrovani`(`IdrReg`)
		ON UPDATE CASCADE;
        
ALTER TABLE `Rezervacija`
	ADD CONSTRAINT `R_8` FOREIGN KEY (`IdObj`) REFERENCES `Objekat`(`IdObj`)
		ON UPDATE CASCADE;



ALTER TABLE `Sto`
	ADD CONSTRAINT `R_2` FOREIGN KEY (`IdObj`) REFERENCES `Objekat`(`IdObj`)
		ON UPDATE CASCADE;


ALTER TABLE `Sto`
	ADD CONSTRAINT `R_3` FOREIGN KEY (`IdTip`) REFERENCES `Tip`(`IdTip`)
		ON UPDATE CASCADE;