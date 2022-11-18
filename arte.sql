-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 15-11-2022 a las 15:30:09
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `arte`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente`
--

CREATE TABLE `cliente` (
  `id` int(11) NOT NULL,
  `nombreCliente` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `telefono` varchar(15) NOT NULL,
  `email` varchar(30) NOT NULL,
  `obraInteres` varchar(50) NOT NULL,
  `direccion` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `cliente`
--

INSERT INTO `cliente` (`id`, `nombreCliente`, `apellido`, `telefono`, `email`, `obraInteres`, `direccion`) VALUES
(1, 'd', 'w', 'w', 'w@g', 'w', 'w'),
(2, 'aw', 'aw', 'aw', 'a@sw', 'aw', 'aw'),
(3, 'a', 'a', 'a', 'a@s', 'a', 'a'),
(4, 'aa', 'a', 'a', 'a@ds', 'a', 's'),
(5, 'q', 'q', 'q', 'l@j', 'qq', 'q'),
(6, 'a', 'a', 'a', 'a@a', 'a', 'ax'),
(7, 'q', 'q', 'q', 'q@s', 's', 's'),
(8, 'q', 'q', 'q', 'q@s', 's', 's');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tabla_pintura`
--

CREATE TABLE `tabla_pintura` (
  `id` int(11) NOT NULL,
  `nombre_obra` varchar(75) NOT NULL,
  `descripcion` varchar(150) NOT NULL,
  `autor` varchar(70) NOT NULL,
  `lugar_elab` varchar(70) NOT NULL,
  `valor` varchar(70) NOT NULL,
  `ubicacion` varchar(70) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `tabla_pintura`
--

INSERT INTO `tabla_pintura` (`id`, `nombre_obra`, `descripcion`, `autor`, `lugar_elab`, `valor`, `ubicacion`) VALUES
(1, 'la noche estrellada', 'w', 'vincent van gogh(\'\'?', 'w', 'w', 'w'),
(3, 'kdskfjskksnsndks', '23', '2222323', '12', '32', 'yuyu'),
(4, '1111', '1111', '1111aaaaaaaaaaaaaaaa', '111', '111', '1111'),
(5, 'p001', 'JEFE DE MERCADOTECNIA', 'NO NECESARIOS', 'MEMORIA A CORTO Y LARGO PLAZO', 'NO ESPECIFICADAS', 'AGRADABLES'),
(38, '8798787', 'PRODUCTOR', 'gggbfggbbgfgfb', 'gfbgfbfgbbgf', 'rrgffgrtgt', 'tgrgtrtgfggssss'),
(50, '111111111111111', 'aaaaaaaaaaaa', 'hhh', 'x', 'x', 'xxx'),
(52, '33', 'ssssssssssss', 'fghj', 'dfgh', 'fghj', 'sdfghj'),
(53, '44444', 'sssssssss', 'h', 'noi', 'okk', 'hhn'),
(54, '123456789', 'wwwwwwwwww', 'bbbbb', 'kk', 'ss', 'ooooooooooooooood'),
(55, '111111111111111', 'dddddddddddddddddda', 'ddddddda', 'dda', 'dddda', 'dddda'),
(56, 'qqqqqqqqqqq@s', 'ijbib', 'sssss', 'ss', 'ss', 'ss'),
(57, 'asdf@fgh', 'dfgh', 'xcg', 'cvbn', 'b', 'b'),
(60, 'a', 'a', 'a', 'a', 'a', 'a');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tabla_subasta`
--

CREATE TABLE `tabla_subasta` (
  `id` int(11) NOT NULL,
  `nombre_obr` varchar(75) NOT NULL,
  `nombre` varchar(110) NOT NULL,
  `valor` int(11) NOT NULL,
  `hora_inicio` varchar(110) NOT NULL,
  `hora_fin` varchar(110) NOT NULL,
  `autor` varchar(100) NOT NULL,
  `juez` varchar(110) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tabla_subasta`
--

INSERT INTO `tabla_subasta` (`id`, `nombre_obr`, `nombre`, `valor`, `hora_inicio`, `hora_fin`, `autor`, `juez`) VALUES
(1, 'w', 'w', 0, 'w', 'w', 'w', 'w'),
(3, 'kdskfjskksnsndks', '23', 2222323, '12', '32', '2222', 'ewdwdwjuanitoperez'),
(4, '1111', '1111', 1111, '111', '111', '1111', '11111'),
(5, 'mujer con sombrilla', 'tods', 7555220, '43', '34', 'monet', 'yo'),
(8, 'sa', 'sa', 0, '88', '99', 'sa', 'saaaaaaa'),
(10, 'aaaaaaaaaaaa', 'aaaaaaaaaa', 9000, 'aaaaaa', 'aaaa', 'aaaaaaa', 'aaaaaaakj'),
(11, 'eqqq', 'e', 99, 'e', 'e', 'e', 'e');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `tabla_pintura`
--
ALTER TABLE `tabla_pintura`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `tabla_subasta`
--
ALTER TABLE `tabla_subasta`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `cliente`
--
ALTER TABLE `cliente`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `tabla_pintura`
--
ALTER TABLE `tabla_pintura`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT de la tabla `tabla_subasta`
--
ALTER TABLE `tabla_subasta`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
