-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 28, 2023 at 02:34 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pythontkinter`
--

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `gender` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `Level` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `pest` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `add` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `note` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `phone` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`gender`, `Level`, `pest`, `add`, `note`, `phone`, `name`, `id`) VALUES
('ذكر', 'حاضر', 'إمتياز', 'مصر', 'مطور البرنامج و المالك الاول لقاعده البيانات', '0538886324', 'محمد علاء محمد ', 1),
('ذكر', 'حاضر', 'جيد', 'مصر', 'ناقص 3 درجات من كل ماده و الحاسب 25 درجه', '0509235041', 'عمار علاء', 2),
('أفضل عدم التحديد', 'حاضر', 'جيد جداً', 'جمصه ', 'طالب جامعي', '002', 'عمرو حسين احمد', 3),
('أنثي', 'حاضر', 'جيد جداً', 'مصر', 'لا ', '0509235041', 'تغريد علاء محمد', 4),
('ذكر', 'حاضر', 'جيد', 'القاهرة', 'لم يجتاز ماده الإستاتيكا حيث حصل علي 58%', '0509237491', 'تامر مرسي', 5),
('أنثي', ' غائب', 'راسب', 'UNno', 'ISRAIER', '009', 'NETINYAHO', 6),
('ذكر', 'حاضر', 'إمتياز', 'مصر 6 اكتوبر', 'طالب جامعي', '002', 'مصطفي', 7),
('ذكر', 'حاضر', 'جيد جداً', 'غير معرف', 'لا يوجد', '999', 'صابر علي', 8),
('ذكر', ' غائب', 'ضغيف', 'jordon', 'not a way', '006354', 'nader mustafa', 9),
('أفضل عدم التحديد', ' غائب', 'راسب', 'امريكا', 'عالم', '04044', 'eidson many', 10),
('ذكر', 'حاضر', 'جيد', 'fonady', 'not way', '0592763913', 'mr ahmed radi', 11),
('ذكر', 'حاضر', 'إمتياز', 'tani', 'facebook', '0032', 'mark zordef', 12),
('أفضل عدم التحديد', ' غائب', 'جيد', 'tailandi', 'no', '008523232323', 'sami', 13),
('غير معروف بدون ذكر', 'حاضر', 'ممتاز', 'MADREEDIR', 'NO AWY', '4543654655555', 'hany', 14),
('أفضل عدم التحديد', ' غائب', 'جيد', 'jeboti', 'no but....', '056669', 'toni', 15),
('ذكر', ' غائب', 'جيد', 'addsori', 'but only owon', '090', 'morkosnabi', 17),
('ذكر', 'حاضر', 'إمتياز', 'dony', 'but any way', '9903332', 'safi', 18),
('ذكر', 'حاضر', 'ممتاز', 'kanada', 'good', '434312', 'fadi', 19),
('أنثي', 'حاضر', 'ممتاز', 'vovidsom', 'xx2|||2waA`', '1234567890', 'sandy', 20),
('أنثي', 'حاضر', 'ممتاز', 'تربه - الطائف - الخرمه', 'لا يوجد', '65777990', 'زينب احمد', 21),
('أفضل عدم التحديد', ' غائب', 'ممتاز', 'الفيوم', 'لا يوجد', '443332', 'جمال', 22);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
