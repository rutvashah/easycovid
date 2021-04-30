-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3307
-- Generation Time: Apr 30, 2021 at 08:36 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `medical`
--

-- --------------------------------------------------------

--
-- Table structure for table `hospital_details`
--

CREATE TABLE `hospital_details` (
  `hid` int(5) NOT NULL,
  `name` varchar(30) DEFAULT NULL,
  `address` varchar(70) DEFAULT NULL,
  `area` varchar(30) DEFAULT NULL,
  `pincode` int(8) DEFAULT NULL,
  `zone` varchar(5) DEFAULT NULL,
  `city` varchar(20) DEFAULT NULL,
  `state` varchar(30) DEFAULT NULL,
  `updated_on` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `hospital_details`
--

INSERT INTO `hospital_details` (`hid`, `name`, `address`, `area`, `pincode`, `zone`, `city`, `state`, `updated_on`) VALUES
(1, 'HCG Hospital', 'Mithakali six rd', 'Navrangpura', 380006, 'WZ', 'Ahmedabad', 'Gujarat', '2021-04-21'),
(2, 'Saviour Annexe Hospital', 'Sardar Patel Stadium Rd, Near Bharat Petrol Pump, Chaitanya Nagar', 'Navrangpura', 380014, 'WZ', 'Ahmedabad', 'Gujarat', '2021-04-21'),
(3, 'Aims Hospitals', ' P.N House, 3rd Floor, Narayan Nagar Rd', 'Paldi', 380007, 'WZ', 'Ahmedabad', 'Gujarat', '2021-04-21'),
(4, 'Bodyline Hospitals', 'Dev Status, Opp Annapurna Hall, Besides, New Vikas Gruh Rd', 'Paldi', 380007, 'WZ', 'Ahmedabad', 'Gujarat', '2021-04-21');

-- --------------------------------------------------------

--
-- Table structure for table `hospital_services`
--

CREATE TABLE `hospital_services` (
  `hospital_id` int(5) DEFAULT NULL,
  `no_of_beds` int(5) DEFAULT NULL,
  `no_of_occupy` int(5) DEFAULT NULL,
  `no_of_empty` int(5) DEFAULT NULL,
  `no_of_venti` int(5) DEFAULT NULL,
  `no_of_remdi` int(5) DEFAULT NULL,
  `no_of_oxygen` int(5) DEFAULT NULL,
  `no_of_ambulance` int(5) DEFAULT NULL,
  `updated_no` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `hospital_services`
--

INSERT INTO `hospital_services` (`hospital_id`, `no_of_beds`, `no_of_occupy`, `no_of_empty`, `no_of_venti`, `no_of_remdi`, `no_of_oxygen`, `no_of_ambulance`, `updated_no`) VALUES
(1, 20, 3, 17, 5, 3, 22, 7, '2021-04-21'),
(2, 21, 2, 19, 7, 4, 30, 12, '2021-04-21'),
(3, 100, 80, 20, 4, 3, 150, 104, '2021-04-21'),
(4, 10, 0, 10, 2, 1, 12, 3, '2021-04-21');

-- --------------------------------------------------------

--
-- Table structure for table `no_of_days`
--

CREATE TABLE `no_of_days` (
  `id` int(5) NOT NULL,
  `days` int(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `no_of_days`
--

INSERT INTO `no_of_days` (`id`, `days`) VALUES
(1, 36);

-- --------------------------------------------------------

--
-- Table structure for table `plasma_donor`
--

CREATE TABLE `plasma_donor` (
  `id` int(5) NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  `phone` bigint(15) DEFAULT NULL,
  `blood` varchar(5) DEFAULT NULL,
  `age` int(3) DEFAULT NULL,
  `negative_date` date DEFAULT NULL,
  `vaccinated` varchar(7) DEFAULT NULL,
  `passed` varchar(7) DEFAULT NULL,
  `surgery` varchar(7) DEFAULT NULL,
  `disease` varchar(7) DEFAULT NULL,
  `days` int(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `plasma_donor`
--

INSERT INTO `plasma_donor` (`id`, `name`, `phone`, `blood`, `age`, `negative_date`, `vaccinated`, `passed`, `surgery`, `disease`, `days`) VALUES
(1, 'Ankit Patel', 9876543210, 'O+', 50, '2021-03-22', 'No', 'No', 'No', 'No', 36),
(2, 'Mona Gupta', 9170225308, 'B-', 48, '2021-04-01', 'No', 'No', 'No', 'No', 29);

-- --------------------------------------------------------

--
-- Table structure for table `tiffin_services`
--

CREATE TABLE `tiffin_services` (
  `id` int(5) DEFAULT NULL,
  `area` varchar(30) DEFAULT NULL,
  `name` varchar(30) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `address` varchar(70) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tiffin_services`
--

INSERT INTO `tiffin_services` (`id`, `area`, `name`, `phone`, `address`) VALUES
(1, 'Sabarmati', 'Annpurna Tiffin Service', 7947360488, 'Chamunda Nagar, Sabarmati, Ahmedabad - 380005, Nea'),
(2, 'Sabarmati', 'Om Sai Tiffin Service', 7947073921, '11 Vaibhav Bunglows, Sabarmati,Opposite D Mart Vis'),
(3, 'Chandkheda', 'Vanshika Tiffin Services', 7947072681, 'A- 68, Bhaktinagar Society, Ioc Road, Chandkheda,B'),
(4, 'Vasna', 'Food Point Tifin Service', 8128838786, 'F/13 Shree Sadan Flat, Vasna, Ahmedabad - 380007, '),
(5, 'Ranip', 'Shree Sharda Tiffin & Catering', 7947072978, 'G 302, Swaminarayan Park 1, Ranip,Near Mangaldeep ');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `hospital_details`
--
ALTER TABLE `hospital_details`
  ADD PRIMARY KEY (`hid`);

--
-- Indexes for table `no_of_days`
--
ALTER TABLE `no_of_days`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `plasma_donor`
--
ALTER TABLE `plasma_donor`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `no_of_days`
--
ALTER TABLE `no_of_days`
  MODIFY `id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `plasma_donor`
--
ALTER TABLE `plasma_donor`
  MODIFY `id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
