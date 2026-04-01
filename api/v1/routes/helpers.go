package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strings"
)

func readConfigFile(filename string) (map[string]string, error) {
	data, err := ioutil.ReadFile(filename)
	if err != nil {
		return nil, err
	}
	return strings.Map(func(rune) string {
		return string(rune)
	}, string(data))
}

func readConfigMap(filename string) (map[string]string, error) {
	data, err := ioutil.ReadFile(filename)
	if err != nil {
		return nil, err
	}
	return map[string]string(data), nil
}

func readConfigMapWithDefaultValues(filename string) (map[string]string, error) {
	data, err := ioutil.ReadFile(filename)
	if err != nil {
		return nil, err
	}
	return map[string]string(data), nil
}