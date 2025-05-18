#include <gpiod.hpp>

auto OUTPUT = ::gpiod::line::direction::OUTPUT;
auto INPUT = ::gpiod::line::direction::INPUT;

::gpiod::line::offset lineSensorEnable = 2;
::gpiod::line::offset lineSensorL = 14;
::gpiod::line::offset lineSensorC = 15;
::gpiod::line::offset lineSensorR = 18;

::gpiod::line::offset motorEnable = 22;
::gpiod::line::offset motorLfwd = 18;
::gpiod::line::offset motorLbwd = 23;
::gpiod::line::offset motorRfwd = 24;
::gpiod::line::offset motorRbwd = 25;

::gpiod::line::offsets inputLines = {
    lineSensorL,
    lineSensorC,
    lineSensorR};

::gpiod::line::offsets outputLines = {
    lineSensorEnable,
    motorEnable,
    motorLfwd,
    motorLbwd,
    motorRfwd,
    motorRbwd};

::gpiod::line::values outputValues = {
    ::gpiod::line::value::INACTIVE,
    ::gpiod::line::value::INACTIVE,
    ::gpiod::line::value::INACTIVE,
    ::gpiod::line::value::INACTIVE,
    ::gpiod::line::value::INACTIVE,
    ::gpiod::line::value::INACTIVE};

int main(int argc, char const *argv[])
{
    ::gpiod::request_config requestConfig{};
    requestConfig.set_consumer("Motorsteuerung");

    ::gpiod::line_config lineConfig{};
    lineConfig.add_line_settings(inputLines, ::gpiod::line_settings().set_direction(INPUT));
    lineConfig.add_line_settings(outputLines, ::gpiod::line_settings().set_direction(OUTPUT));
    lineConfig.set_output_values(outputValues);

    auto request = ::gpiod::chip("/dev/gpiochip0")
                       .prepare_request()
                       .set_request_config(requestConfig)
                       .set_line_config(lineConfig)
                       .do_request();

    return 0;
}
